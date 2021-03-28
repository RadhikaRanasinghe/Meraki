import base64
import io
import os
from PIL import Image, ImageFile
from User import User
from TestImageBuilder import TestImageBuilder
from UserModel import UserModel
import pickle

ImageFile.LOAD_TRUNCATED_IMAGES = True


class Detector:
    __user: User = None

    def load_features(self, image_no: UserModel):
        """The function to load the features from the image and stores them in a TestImage object. Thius object is
        stored in a User object.

        Args:
            image_no (UserModel): the details of the user
        """
        img = Image.open(io.BytesIO(image_no.get_test_image()))  # byte is converted to image
        img.save('images/image' + str(image_no.get_id()) + '.jpg')  # the image file is stored as a .jpg file

        # TODO: Run the C++ file.

        # temp testing
        img.save('images/image' + str(image_no.get_id()) + '_pen.jpg')
        img.save('images/image' + str(image_no.get_id()) + '_template.jpg')

        img.close()
        os.remove('images/image' + str(image_no.get_id()) + '.jpg')  # Image files are removed
        os.remove('images/image' + str(image_no.get_id()) + '_pen.jpg')
        os.remove('images/image' + str(image_no.get_id()) + '_template.jpg')

        feature_file = open("results/RMS" + str(image_no.get_id()) + ".txt",
                            "r")  # features from the RMS.txt file are taken
        features = feature_file.read()
        feature_file.close()
        features = features.split(", ")

        # the features are stored in the test_image object
        test_image = TestImageBuilder() \
            .set_rms(float(features[1])) \
            .set_std_deviation_st_ht(float(features[2])) \
            .set_max_between_st_ht(float(features[3])) \
            .set_min_between_st_ht(features[4]) \
            .set_mrt(float(features[5])) \
            .set_max_ht(float(features[6])) \
            .set_min_ht(features[7]) \
            .set_std_ht(float(features[8])) \
            .set_changes_from_negative_to_positive_between_st_ht(float(features[9])) \
            .build()

        # User object is created
        self.__user = User(
            test_image=test_image,
            age=image_no.get_age(),
            gender=image_no.get_gender(),
            handedness=image_no.get_handedness())
        os.remove("results/RMS" + str(image_no.get_id()) + ".txt")

    def process(self) -> bool:
        result: bool = True

        with open('Models/ensemble_classifier.pickle', 'rb') as file:
            ensemble_classifier = pickle.load(file)

        x = [[self.__user.get_gender(), self.__user.get_handedness(), self.__user.get_age(),
              self.__user.get_test_image().get_rms(), self.__user.get_test_image().get_max_ht(),
              self.__user.get_test_image().get_min_ht(), self.__user.get_test_image().get_std_deviation_st_ht(),
              self.__user.get_test_image().get_mrt(), self.__user.get_test_image().get_max_ht(),
              self.__user.get_test_image().get_min_ht(), self.__user.get_test_image().get_std_ht(),
              self.__user.get_test_image().get_changes_from_negative_to_positive_between_st_ht()]]

        y_pred = ensemble_classifier.predict(x)
        print(y_pred)

        if y_pred == 2:
            result = True
        elif y_pred == 1:
            result = False

        return result

    def get_user(self) -> User:
        return self.__user

    def set_user(self, user: User):
        self.__user = user
