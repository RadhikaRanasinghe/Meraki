from User import User
from UserModel import UserModel


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

    def process(self, image_no: int) -> bool:
        result: bool = True

        # TODO: Run data science .py file or do it here.

        # TODO: Return the output.

        return result

    def get_user(self) -> User:
        return self.__user

    def set_user(self, user: User):
        self.__user = user
