from .TestImage import TestImage


class User:
    def __init__(self, __test_image, __age, __gender, __handedness):
        self.__test_image: TestImage = __test_image
        self.__age: int = __age
        self.__gender: str = __gender
        self.__handedness: str = __handedness

        def get_age(self) -> int:
            return self.__age

        def set_age(self, __age):
            self.__age = __age

        def get_gender(self) -> str:
            return self.__gender

        def set_gender(self, __gender):
            self.__gender = __gender

        def get_handedness(self) -> str:
            return self.__handedness

        def set_handedness(self, __handedness):
            self.__handedness = __handedness

        def get_testImage(self) -> TestImage:
            return self.__test_image

        def set_testImage(self, __test_image: TestImage):
            self.__test_image = __test_image
