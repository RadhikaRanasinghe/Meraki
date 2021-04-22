import pickle
import time

from TestImageBuilder import TestImageBuilder
from User import User
from UserModel import UserModel

import requests


class Detector:
    """
    This class is used to get the user details from the database and then extracting the exam template and the
    hand drawn image from image provided by the user. These two images are compared and the features are extracted. 
    These features are used by the voting classifier to get the prediction. The prediction is returned.
    """

    __user: User = None

    def load_features(self, test: UserModel):
        """The function to load the features from the image and stores them in a TestImage object. Thius object is
                    stored in a User object.

        :param test: the details of the user
        """

        # Requesting the image extraction details from lambda.
        test_image_dict = None
        for i in range(20):
            print(f"Requesting OpenCV results {test.get_id()}, try {i}...")
            x = requests.get('https://9e98utlj5i.execute-api.us-east-2.amazonaws.com/test/transactions',
                             params={"image_no": str(test.get_id())})
            print(x.status_code, x.json())
            # Checking if an OK result is coming.
            if x.status_code == 200:
                # Checking if the result is received.
                if x.json()['test_image'] is None:
                    # When OpenCV lambda crashes.
                    if i == 0:
                        break
                    time.sleep(15)
                    continue
                # When the result is received.
                else:
                    test_image_dict = x.json()['test_image']
                    break
            # When a bad Gateway or other server errors happen.
            else:
                time.sleep(15)

        # When a result is not received.
        if test_image_dict is None:
            print(f"ERROR - OpenCV results {test.get_id()} didn't received")
            test_image = None
        # When a result is received.
        else:
            print(f"OpenCV results {test.get_id()} received")
            test_image = TestImageBuilder() \
                .set_rms(test_image_dict['rms']) \
                .set_std_deviation_st_ht(test_image_dict['rms']) \
                .set_max_between_st_ht(test_image_dict['rms']) \
                .set_min_between_st_ht(test_image_dict['rms']) \
                .set_mrt(test_image_dict['rms']) \
                .set_max_ht(test_image_dict['rms']) \
                .set_min_ht(test_image_dict['rms']) \
                .set_std_ht(test_image_dict['rms']) \
                .set_changes_from_negative_to_positive_between_st_ht(test_image_dict['rms']) \
                .build()

        # User object is created
        self.__user = User(
            test_image=test_image,
            age=test.get_age(),
            gender=test.get_gender(),
            handedness=test.get_handedness())

    def process(self):
        """
        This function loads the pickle file of the voting classifier model and takes the features returned
        by the function load features. The function then predicts the accordingly and returns the result.

        :return:A variable called 'result' of type boolean containing the result predicted by the voting classifier

        """

        if self.__user.get_test_image() is None:
            return None
        else:
            # Initializing and assigning the variable 'result' to True
            result = None

            # Loading the features into a list and assigning it as 'x'
            x = [[self.__user.get_gender(), self.__user.get_handedness(), self.__user.get_age(),
                  self.__user.get_test_image().get_rms(), self.__user.get_test_image().get_max_ht(),
                  self.__user.get_test_image().get_min_ht(), self.__user.get_test_image().get_std_deviation_st_ht(),
                  self.__user.get_test_image().get_mrt(), self.__user.get_test_image().get_max_ht(),
                  self.__user.get_test_image().get_min_ht(), self.__user.get_test_image().get_std_ht(),
                  self.__user.get_test_image().get_changes_from_negative_to_positive_between_st_ht()]]

            # Opening the voting classifier pickle file and storing the model in the variable 'ensemble_classifier'
            with open('models/VotingClassifier.pickle', 'rb') as file:
                ensemble_classifier = pickle.load(file)

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
