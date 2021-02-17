class User:
    def __init__(self, __testImage, __age, __gender, __handedness):
        self.__testImage = __testImage
        self.__age = __age
        self.__gender = __gender
        self.__handedness = __handedness

        def get_age():
            return self.__age

        def set_age(__age):
            self.__age = __age

        def get_gender():
            return self.__gender

        def set_gender(__gender):
            self.__gender = __gender

        def get_handedness(__handedness):
            self.__handedness = __handedness




