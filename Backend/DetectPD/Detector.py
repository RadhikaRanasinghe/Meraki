from User import User
from UserModel import UserModel
import pickle


class Detector:
    __user: User = None

    def __init__(self):
        pass

    def load_features(self, image_no: UserModel):
        # TODO: GET the image from the database.

        # TODO: Run the C++ file.

        # TODO: Read RMS.txt(assume its a csv).

        # TODO: Fill the __user variable.

        pass

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
