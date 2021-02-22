from User import User


class Detector:
    __user: User = None

    def __init__(self):
        pass

    def load_features(self, image_no: int):
        # self.__image_no = image_no
        pass

    def process(self, image_no: int) -> bool:
        result: bool = None
        return result

    def get_user(self) -> User:
        return self.__user

    def set_user(self, user: User):
        self.__user = user
