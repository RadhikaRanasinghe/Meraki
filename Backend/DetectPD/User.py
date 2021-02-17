from TestImage import TestImage


class User:
    def __init__(self, __test_image: TestImage, __age: int, __gender: int, __handedness: int):
        self.__test_image: TestImage = __test_image
        self.__age: int = __age
        self.__gender: int = __gender
        self.__handedness: int = __handedness

        def get_age(self) -> int:
            return self.__age

        def set_age(self, __age: int):
            self.__age = __age

        def get_gender(self) -> int:
            return self.__gender

        def set_gender(self, __gender: int):
            self.__gender = __gender

        def get_handedness(self) -> int:
            return self.__handedness

        def set_handedness(self, __handedness: int):
            self.__handedness = __handedness

        def get_test_image(self) -> TestImage:
            return self.__test_image

        def set_test_image(self, __test_image: TestImage):
            self.__test_image = __test_image
