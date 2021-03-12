from flask import Flask, request, jsonify

import mysql_connection as conn
from Detector import Detector
from TestImage import TestImage

application = Flask(__name__)


@application.route('/', methods=['GET'])
def hello_world():
    return "Hello World"


@application.route('/create_user', methods=['POST'])
def create_user():

    payload = request.form.to_dict()

    if 'image' in request.files and payload.keys() >= {'age', 'gender', 'handedness'}:
        file = request.files['image']

        age = payload['age']
        gender = payload['gender']
        handedness = payload['handedness']

        if age.isdigit() and gender.isdigit() and handedness.isdigit() and \
                'image/' in file.headers.get('Content-Type')[:6]:
            age = int(age)
            gender = int(gender)
            handedness = int(handedness)

            image = file.read()

            user_id = conn.insert_values_test(age, gender, handedness, image)

            return jsonify({"image_no": user_id}), 201
        else:
            return jsonify({"image_no": 0}), 415
    else:
        return jsonify({"image_no": 0}), 400


@application.route('/retrieve_result', methods=['GET'])
def retrieve_result():
    if 'image_no' in request.args:
        image_no = request.args.get('image_no')

        if image_no.isdigit():
            image_no = int(image_no)

            user_model = conn.select_record_test(image_no)

            if user_model != 0:
                test_image_id = user_model.get_test_image_id()

                if test_image_id == 0:

                    detector = Detector()

                    detector.load_features(user_model)
                    result = detector.process(image_no)

                    # test_image = detector.get_user().get_test_image()
                    test_image = TestImage()
                    test_image.set_rms(1.01)
                    test_image.set_mrt(2.02)
                    test_image.set_std_ht(3.03)
                    test_image.set_min_ht(4.3)
                    test_image.set_max_ht(5.4)
                    test_image.set_min_between_st_ht(6.3)
                    test_image.set_max_between_st_ht(7.4)
                    test_image.set_std_deviation_st_ht(8.5)
                    test_image.set_changes_from_negative_to_positive_between_st_ht(9.01)
                    conn.insert_values_test_image(test_image, image_no, result)

                    return jsonify({"result": result}), 200
                else:
                    result = conn.select_test_image_result(test_image_id)
                    return jsonify({"result": result}), 200
            else:
                return jsonify({"result": 0}), 404
        else:
            return jsonify({"result": 0}), 415
    else:
        return jsonify({"result": 0}), 400


if __name__ == '__main__':
    application.run()
