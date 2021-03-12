from User import User
from UserModel import UserModel
from TestImageBuilder import TestImageBuilder
import io
import base64
import PIL.Image as Image
import os

__user: User = None


class Detector:

    def __init__(self):
        pass

    def load_features(self, image_no: UserModel):
        # TODO: GET the image from the database.
        b = base64.b64encode(UserModel.get_test_image())
        img = Image.open(io.BytesIO(b))
        img.save('/images/image' + str(UserModel.get_test_image_id()) + '.png')

        # TODO: Run the C++ file.

        # TODO: Read RMS.txt(assume its a csv).
        os.remove('/images/image' + str(UserModel.get_test_image_id()) + '.png')
        feature_file = open("RMS.txt", "r")
        features = feature_file.read()
        features = features.split(" ")

        # TODO: Fill the __user variable.
        test_image = TestImageBuilder.build(features[0], features[1], features[2], features[3], features[4],
                                            features[5],
                                            features[6], features[7], features[8])

        self.__user.set_test_image(test_image)
        self.__user.set_age(image_no.get_age())
        self.__user.set_gender(image_no.get_gender())
        self.__user.set_handedness(image_no.get_handedness())

    def process(self, image_no: int) -> bool:
        result: bool = None

        # TODO: Run data science .py file or do it here.

        # TODO: Return the output.

        return result

    def get_user(self) -> User:
        return self.__user

    def set_user(self, user: User):
        self.__user = user
