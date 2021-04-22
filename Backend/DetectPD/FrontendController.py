from flask import Flask, request, jsonify, redirect

import mysql_connection as conn
from Detector import Detector

application = Flask(__name__)


@application.route('/')
def about_pd():
    """
    Method for the root URL of the API.
    :return: A String containing 'Hello DetectPD'.
    """
    print("Hello DetectPD")
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
            print(f"OK 200 - image_no: {user_id}")
            return jsonify({"image_no": user_id}), 201
        else:
            message = "Invalid input type. \n'age'/'gender'/'handedness' - Integer, \n'image' - jpg/jpeg image"
            info = f"ERROR 415 - age: {age}, gender: {gender}, handedness: {handedness}, " \
                   f"image: {file.headers.get('Content-Type')}"
            print(info)
            return jsonify({"error": message, 'info': info}), 415
    else:
        info = f"ERROR 400 - age: {'age' in payload.keys()}, gender: {'gender' in payload.keys()}, " \
               f"handedness: {'handedness' in payload.keys()}, image: {'image' in request.files}"
        print(info)
        return jsonify({"error": "Missing input. \n'age', 'gender', 'handedness', 'image' is required.", 'info': info}), 400


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

                    if result is None:
                        return jsonify({"error": "Server could not determine a proper result."}), 510
                    else:
                        # Saving the test result to RDS.
                        conn.insert_result_test_image(image_no, result)

                        # Return the test result.
                        print(f"OK 200 - result: {result}")
                        return jsonify({"result": result}), 200
                # When reprocessed result is available.
                else:
                    # Loading the preprocessed result.
                    result = conn.select_test_image_result(test_image_id)
                    # Return the test result.
                    print(f"OK 200 - result: {result}")
                    return jsonify({"result": result}), 200
            else:
                info = f"ERROR 416 - image_no: {image_no}"
                print(info)
                return jsonify({"error": "Invalid image_no, No such id exists in the database.", 'info': info}), 416
        else:
            info = f"ERROR 415 - image_no: {image_no}"
            print(info)
            return jsonify({"error": "Invalid input type. \n'image_no' - Integer", 'info': info}), 415
    else:
        info = f"ERROR 400 - image_no: {'image_no' in request.args}"
        print(info)
        return jsonify({"error": "Missing input. \n'image_no' is required.", 'info': info}), 400


if __name__ == '__main__':
    application.run(debug=False)
