from PIL import Image
from flask import Flask, request, jsonify, abort
from flask_restful import Api, Resource, reqparse, fields, marshal_with
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)

get_args = reqparse.RequestParser()
get_args.add_argument("image_no", type=int, help="Image Number is required", required=True)

post_args = reqparse.RequestParser()
post_args.add_argument("image", type=bin, help="Image is required", required=True)
post_args.add_argument("age", type=int, help="Age is required", required=True)
post_args.add_argument("gender", type=int, help="Gender is required", required=True)
post_args.add_argument("handedness", type=int, help="Handedness is required", required=True)


class UserModel(db.Model):
    image_no = db.Column(db.Integer, primary_key=True, autoincrement=True)
    age = db.Column(db.Integer)
    gender = db.Column(db.Integer)
    handedness = db.Column(db.Integer)

    def __repr__(self):
        return f"image_no={self.image_no}, age={self.age}, gender={self.gender}, handedness={self.handedness}"


# db.create_all()

resource_fields = {
    'image_no': fields.Integer,
    'age': fields.Integer,
    'gender': fields.Integer,
    'handedness': fields.Integer
}


@app.route('/create_user', methods=['POST'])
@marshal_with(resource_fields)
def create_user():
    # TODO: write a function to check whether every input is there.

    file = request.files['image']
    payload = request.form.to_dict()

    age = payload['age']
    gender = payload['gender']
    handedness = payload['handedness']

    user = UserModel(age=age, gender=gender, handedness=handedness)
    db.session.add(user)
    db.session.commit()

    image_no = user.image_no

    # TODO: change this to whatever storage.
    file.save(f'images/{image_no}.png')

    return user, 201


@app.route('/retrieve_result/<int:image_no>', methods=['GET'])
def retrieve_result(image_no):
    result = UserModel.query.filter_by(id=image_no).first()
    if not result:
        abort(404, message="Could not find Image with that image_no")

    age = result['age']
    gender = result['gender']
    handedness = result['handedness']

    # TODO: Run the C++ file.

    # TODO: Read the RMS.txt and RUN the models

    return jsonify({"result": True})


if __name__ == '__main__':
    app.run(debug=True)
