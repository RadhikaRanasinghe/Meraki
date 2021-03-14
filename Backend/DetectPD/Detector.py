import base64
import io
import os
import PIL.Image as Image
from TestImageBuilder import TestImageBuilder
from User import User
from UserModel import UserModel


class Detector:
    __user: User = None

    def __init__(self):
        pass

    def load_features(self, image_no: UserModel):
        b = base64.b64decode(UserModel.get_test_image(image_no))
        img = Image.open(io.BytesIO(b))
        img.save('images/image' + str(UserModel.get_test_image_id(image_no)) + '.png')

        # TODO: Run the C++ file.

        os.remove('/images/image' + str(UserModel.get_test_image_id(image_no)) + '.png')
        feature_file = open("RMS.txt", "r")
        features = feature_file.read()
        features = features.split(" ")

        test_image = TestImageBuilder()
        test_image.set_rms(float(features[1]))
        test_image.set_std_deviation_st_ht(float(features[2]))
        test_image.set_max_between_st_ht(float(features[3]))
        test_image.set_min_between_st_ht(float(features[4]))
        test_image.set_mrt(float(features[5]))
        test_image.set_max_ht(float(features[6]))
        test_image.set_min_ht(float(features[7]))
        test_image.set_std_ht(float(features[8]))
        test_image.set_changes_from_negative_to_positive_between_st_ht(float(features[9]))

        self.__user.set_test_image(test_image)
        self.__user.set_age(image_no.get_age())
        self.__user.set_gender(image_no.get_gender())
        self.__user.set_handedness(image_no.get_handedness())

        pass

    def process(self, image_no: int) -> bool:
        result: bool = True

        # TODO: Run data science .py file or do it here.

        # TODO: Return the output.

        return result

    def get_user(self) -> User:
        return self.__user

    def set_user(self, user: User):
        self.__user = user
