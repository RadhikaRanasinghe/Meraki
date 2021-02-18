from PIL import Image
from flask import Flask, request, jsonify
from flask_restful import Api, Resource, reqparse

app = Flask(__name__)
# api = Api(app)

get_args = reqparse.RequestParser()
get_args.add_argument("image_no", type=int, help="Image Number is required", required=True)

post_args = reqparse.RequestParser()
post_args.add_argument("image", type=bin, help="Image is required", required=True)
post_args.add_argument("age", type=int, help="Age is required", required=True)
post_args.add_argument("gender", type=int, help="Gender is required", required=True)
post_args.add_argument("handedness", type=int, help="Handedness is required", required=True)


# class FrontendController(Resource):
#     def get(self):
#         return
#
#     def post(self):
#         args = post_args.parse_args()
#         return args
#
#
# api.add_resource(FrontendController, "/")


@app.route('/create_user', methods=['POST'])
def create_user():
    # TODO: write a function to check whether every input is there.

    file = request.files['image']
    payload = request.form.to_dict()

    # TODO: Save this however.
    age = payload['age']
    gender = payload['gender']
    handedness = payload['handedness']

    # TODO: Auto generate this.
    image_no = 9

    # TODO: change this to whatever storage.
    file.save(f'images/{image_no}.png')

    return jsonify({"image_no": image_no}), 201


@app.route('/retrieve_result/<int:image_no>', methods=['GET'])
def retrieve_result(image_no):
    # TODO: Run the C++ file.

    # TODO: Read the RMS.txt and RUN the models

    return jsonify({"result": True})


if __name__ == '__main__':
    app.run(debug=True)
