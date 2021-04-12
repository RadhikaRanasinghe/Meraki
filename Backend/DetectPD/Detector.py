import io
import os
import pickle

import cv2
import numpy as np
from PIL import Image, ImageFile

from TestImageBuilder import TestImageBuilder
from User import User
from UserModel import UserModel
from extractFeats import extractFeats
from extractPen import extractPen

ImageFile.LOAD_TRUNCATED_IMAGES = True


class Detector:
    __user: User = None

    def load_features(self, image_no: UserModel):
        # img = Image.open(io.BytesIO(image_no.get_test_image()))
        # img.save('images/image' + str(image_no.get_id()) + '.jpg')

        nparr = np.fromstring(image_no.get_test_image(), np.uint8)
        img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
        cv2.imshow('output', img)
        cv2.waitKey(0)

        img_pen = extractPen(img)
        test_image = extractFeats(img, img_pen)

        # # TODO: Run the C++ file.
        #
        # # temp testing
        # img.save('images/image' + str(image_no.get_id()) + '_pen.jpg')
        # img.save('images/image' + str(image_no.get_id()) + '_template.jpg')
        #
        # img.close()
        # os.remove('images/image' + str(image_no.get_id()) + '.jpg')
        # os.remove('images/image' + str(image_no.get_id()) + '_pen.jpg')
        # os.remove('images/image' + str(image_no.get_id()) + '_template.jpg')
        #
        # feature_file = open("results/RMS" + str(image_no.get_id()) + ".txt", "r")
        # features = feature_file.read()
        # feature_file.close()
        # features = features.split(", ")
        #
        # test_image = TestImageBuilder() \
        #     .set_rms(float(features[1])) \
        #     .set_std_deviation_st_ht(float(features[2])) \
        #     .set_max_between_st_ht(float(features[3])) \
        #     .set_min_between_st_ht(features[4]) \
        #     .set_mrt(float(features[5])) \
        #     .set_max_ht(float(features[6])) \
        #     .set_min_ht(features[7]) \
        #     .set_std_ht(float(features[8])) \
        #     .set_changes_from_negative_to_positive_between_st_ht(float(features[9])) \
        #     .build()

        self.__user = User(
            test_image=test_image,
            age=image_no.get_age(),
            gender=image_no.get_gender(),
            handedness=image_no.get_handedness())
        # os.remove("results/RMS" + str(image_no.get_id()) + ".txt")

    def process(self) -> bool:
        """
        This function loads the pickle file of the voting classifier model and takes the features returned
        by the function load features. The function then predicts the accordingly and returns the result.

        :return:A variable called 'result' containing a boolean containing the result predicted by the voting classifier

        """

        # Initializing and assigning the variable 'result' to True
        result: bool = True

        # Opening the voting classifier pickle file and storing the model in the variable 'ensemble_classifier'
        with open('models/ensemble_classifier.pickle', 'rb') as file:
            ensemble_classifier = pickle.load(file)

        # Loading the features into a list and assigning it as 'x'
        x = [[self.__user.get_gender(), self.__user.get_handedness(), self.__user.get_age(),
              self.__user.get_test_image().get_rms(), self.__user.get_test_image().get_max_ht(),
              self.__user.get_test_image().get_min_ht(), self.__user.get_test_image().get_std_deviation_st_ht(),
              self.__user.get_test_image().get_mrt(), self.__user.get_test_image().get_max_ht(),
              self.__user.get_test_image().get_min_ht(), self.__user.get_test_image().get_std_ht(),
              self.__user.get_test_image().get_changes_from_negative_to_positive_between_st_ht()]]

        # Predicting the result using the loaded features of the user
        y_pred = ensemble_classifier.predict(x)

        # If the predicted result returns '2', then assign result as True
        if y_pred == 2:
            result = True

        # If the predicted result returns '1', then assign result as False
        elif y_pred == 1:
            result = False

        return result

    def get_user(self) -> User:
        return self.__user

    def set_user(self, user: User):
        self.__user = user
