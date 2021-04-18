import pickle

import cv2
import numpy as np

from User import User
from UserModel import UserModel
from extractFeats import extractFeats
from extractPen import extractPen


class Detector:
    __user: User = None

    def load_features(self, image_no: UserModel):
        nparr = np.fromstring(image_no.get_test_image(), np.uint8)
        img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

        img_pen = extractPen(img)
        test_image = extractFeats(img, img_pen)

        self.__user = User(
            test_image=test_image,
            age=image_no.get_age(),
            gender=image_no.get_gender(),
            handedness=image_no.get_handedness())

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
