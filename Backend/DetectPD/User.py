from .TestImage import TestImage


class User:
    def __init__(self, __testImage, __age, __gender, __handedness):
        self.__testImage: TestImage = __testImage
        self.__age: int = __age
        self.__gender: str = __gender
        self.__handedness: str = __handedness

        def get_age() -> int:
            return self.__age

        def set_age(__age):
            self.__age = __age

        def get_gender() -> str:
            return self.__gender

        def set_gender(__gender):
            self.__gender = __gender

        def get_handedness() -> str:
            return self.__handedness

        def set_handedness(__handedness):
            self.__handedness = __handedness

        def get_testImage() -> TestImage:
            return __testImage

        def set_testImage(__testImage):
            self.__testImage = __testImage
