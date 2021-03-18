class UserModel:
    def __init__(self, user_id: int, age: int, gender: int, handedness: int, test_image: bytes, test_image_id: int):
        self.__id: int = user_id
        self.__age: int = age
        self.__gender: int = gender
        self.__handedness: int = handedness
        self.__test_image: bytes = test_image
        self.__test_image_id: int = test_image_id

    def __str__(self):
        return f"UserModel{{id={self.__id}, age={self.__age}, gender={self.__gender}, handedness={self.__handedness}," \
               f" test_image={self.__test_image}}} "

    def get_id(self) -> int:
        return self.__id

    def set_id(self, user_id: int):
        self.__id = user_id

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

    def get_test_image(self) -> bytes:
        return self.__test_image

    def set_test_image(self, test_image: bytes):
        self.__test_image = test_image

    def get_test_image_id(self) -> int:
        return self.__test_image_id

    def set_test_image_id(self, test_image_id: int):
        self.__test_image = test_image_id
