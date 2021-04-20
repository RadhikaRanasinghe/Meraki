import pickle

import cv2
import numpy as np

from User import User
from UserModel import UserModel
from extractFeats import extractFeats
from extractPen import extractPen


class Detector:
    """
    This class is used to get the user details from the database and then extracting the exam template and the
    hand drawn image from image provided by the user. These two images are compared and the features are extracted. 
    These features are used by the voting classifier to get the prediction. The prediction is returned.
    """

    __user: User = None

    def load_features(self, image_no: UserModel):
        """The function to load the features from the image and stores them in a TestImage object. Thius object is
                    stored in a User object.

        :param image_no: the details of the user
        """

        # Converting byte to Image and saving them in he RAM
        nparr = np.fromstring(image_no.get_test_image(), np.uint8)
        img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

        # loading the feature of the image
        img_pen = extractPen(img)
        test_image = extractFeats(img, img_pen)

        # User object is created
        self.__user = User(
            test_image=test_image,
            age=image_no.get_age(),
            gender=image_no.get_gender(),
            handedness=image_no.get_handedness())

    def process(self) -> bool:
        """
        This function loads the pickle file of the voting classifier model and takes the features returned
        by the function load features. The function then predicts the accordingly and returns the result.

        :return:A variable called 'result' of type boolean containing the result predicted by the voting classifier

        """

        # Initializing and assigning the variable 'result' to True
        result: bool = True

        # Opening the voting classifier pickle file and storing the model in the variable 'ensemble_classifier'
        with open('models/VotingClassifier.pickle', 'rb') as file:
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
        """
        Getter of the user

        :return : An User object
        """
        return self.__user

    def set_user(self, user: User):
        """
        Setter of the user

        :param user: An User object
        """
        self.__user = user
