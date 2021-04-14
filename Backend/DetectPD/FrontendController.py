from flask import Flask, request, jsonify

import mysql_connection as conn
from Detector import Detector

application = Flask(__name__)


@application.route('/')
def hello_world():
    """
    Method for the Root URL.
    :return: String Containing 'Hello DetectPD'.
    """
    return "Hello DetectPD"


@application.route('/create_user', methods=['POST'])
def create_user():
    """
    Method to handle POST request to get the user details and test details.
    :return: An Integer (image_no), primary key of the RDS database where it is saved.
    """

    # Loading the text fields received from the request.
    payload = request.form.to_dict()

    # Checking if all the required fields are there.
    if 'image' in request.files and payload.keys() >= {'age', 'gender', 'handedness'}:
        # Loading the image.
        file = request.files['image']

        # Loading text field details.
        age = payload['age']
        gender = payload['gender']
        handedness = payload['handedness']

        # checking all input data are correct format.
        if age.isdigit() and gender.isdigit() and handedness.isdigit() and \
                'image/jpeg' in file.headers.get('Content-Type'):
            # converting all string text fields to integers.
            age = int(age)
            gender = int(gender)
            handedness = int(handedness)
            # Converting the image to a byte string.
            image = file.read()

            # Saving to the RDS MYSQL database.
            user_id = conn.insert_values_test(age, gender, handedness, image)

            # Returning the primary key of the RDS database record.
            return jsonify({"image_no": user_id}), 201
        else:
            return jsonify({"error": "Invalid input type"}), 415
    else:
        return jsonify({"error": "Missing input"}), 400


@application.route('/retrieve_result', methods=['GET'])
def retrieve_result():
    """
    Method to send user the result of the test.
    :return: A boolean, 'true' if PD is detected, 'false' if PD is not detected.
    """

    # Checking if all the required fields are there.
    if 'image_no' in request.args:
        image_no = request.args.get('image_no')

        # checking all input data are correct format.
        if image_no.isdigit():
            # converting all string text fields to integers.
            image_no = int(image_no)

            # Getting the test details from the RDS database.
            user_model = conn.select_record_test(image_no)

            # Checking if the test details loaded properly.
            if user_model != 0:
                # Getting the preprocessed result data if available.
                test_image_id = user_model.get_test_image_id()

                # When preprocessed result is not available.
                if test_image_id == 0:
                    # Processing the user input test.
                    detector = Detector()
                    detector.load_features(user_model)
                    result = detector.process()

                    # Saving the test process details to RDS.
                    test_image = detector.get_user().get_test_image()
                    conn.insert_values_test_image(test_image, image_no, result)

                    # Return the test result.
                    return jsonify({"result": result}), 200
                # When reprocessed result is available.
                else:
                    # Loading the preprocessed result.
                    result = conn.select_test_image_result(test_image_id)
                    # Return the test result.
                    return jsonify({"result": result}), 200
            else:
                return jsonify({"error": "No such id exists in the database"}), 416
        else:
            return jsonify({"error": "Invalid input type"}), 415
    else:
        return jsonify({"error": "Missing input"}), 400


if __name__ == '__main__':
    application.run(debug=True)
