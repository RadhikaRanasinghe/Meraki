from TestImage import TestImage


class User:
    def __init__(self, test_image: TestImage, age: int, gender: int, handedness: int):
        """this is the constructor

        Args:
            test_image (TestImage): TestImage object
            age (int): age of the user
            gender (int): gender of the user
            handedness (int): handednes of the user
        """
        self.__test_image: TestImage = test_image
        self.__age: int = age
        self.__gender: int = gender
        self.__handedness: int = handedness

    def get_age(self) -> int:
        return self.__age

    def set_age(self, age: int):
        self.__age = age

    def get_gender(self) -> int:
        return self.__gender

    def set_gender(self, gender: int):
        self.__gender = gender

    def get_handedness(self) -> int:
        return self.__handedness

    def set_handedness(self, handedness: int):
        self.__handedness = handedness

    def get_test_image(self) -> TestImage:
        return self.__test_image

    def set_test_image(self, test_image: TestImage):
        self.__test_image = test_image
