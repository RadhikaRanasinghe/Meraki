from flask import Flask, request, jsonify
import base64
import io
from PIL import Image

app = Flask(__name__)


# @app.route('/')
# def hello_world():
#     return 'Hello World!'

@app.route("/im_size", methods=["POST"])
def process_image():
    file = request.files['image']
    payload = request.form.to_dict()
    age = payload['age']
    gender = payload['gender']
    handedness = payload['handedness']
    # Read the image via file.stream
    img = Image.open(file.stream)
    file.save('im-received.png')
    # return jsonify({'msg': 'success'}), 201
    return jsonify({'msg': 'success', 'size': [img.width, img.height], 'age': age, 'gender': gender, 'handedness': handedness}), 201


if __name__ == '__main__':
    app.run(debug=True)
