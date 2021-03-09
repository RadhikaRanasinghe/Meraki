from flask import Flask, request, jsonify
import mysql_connection as conn
from Detector import Detector

app = Flask(__name__)


@app.route('/create_user', methods=['POST'])
def create_user():

    payload = request.form.to_dict()

    if 'image' in request.files and payload.keys() >= {'age', 'gender', 'handedness'}:
        file = request.files['image'].read()

        age = int(payload['age'])
        gender = int(payload['gender'])
        handedness = int(payload['handedness'])

        user_id = conn.insert_values_test(age, gender, handedness, file)

        return jsonify({"image_no": user_id}), 201
    else:
        return jsonify({"image_no": 0}), 400


@app.route('/retrieve_result', methods=['GET'])
def retrieve_result():

    if 'image_no' in request.args:
        image_no = int(request.args.get('image_no'))

        user_model = conn.select_record(image_no)

        if user_model != 0:

            detector = Detector()

            detector.load_features(user_model)

            result = detector.process(image_no)

            conn.insert_values_test_image(detector.get_user().get_test_image(), image_no)

            return jsonify({"result": result}), 200
        else:
            return jsonify({"result": 0}), 204
    else:
        return jsonify({"result": 0}), 400


if __name__ == 'FrontendController':
    app.run(debug=True)
