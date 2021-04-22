class UserModel:
    """
    This class is used to create the UserModel object
    """

    def __init__(self, user_id: int, age: int, gender: int, handedness: int, test_image: bytes, test_image_id: int):
        """
        This is the constructor

        :param user_id : id of the user
        :param age : age of the user
        :param gender : gender of the user
        :param handedness : handedness of the user
        :param test_image : testImage object
        :param test_image_id : id of the test image object
        """
        self.__id: int = user_id
        self.__age: int = age
        self.__gender: int = gender
        self.__handedness: int = handedness
        self.__test_image: bytes = test_image
        self.__test_image_id: int = test_image_id

    def __str__(self):
        """
        This function returns the details of the user model object
        """
        return f"UserModel{{id={self.__id}, age={self.__age}, gender={self.__gender}, handedness={self.__handedness}," \
               f" test_image={type(self.__test_image)}}} "

    def get_id(self) -> int:
        """
        Setter of the user_id

        :return: An integer containing the user_id
        """
        return self.__id

    def set_id(self, user_id: int):
        """
        Setter of the user_id

        :param user_id: An integer containing the user_id
        """
        self.__id = user_id

    def get_age(self) -> int:
        """
        Getter of the age

        :return: An integer containing the age
        """
        return self.__age

    def set_age(self, age: int):
        """
        Setter of the age

        :param age: An integer containing the age
        """
        self.__age = age

    def get_gender(self) -> int:
        """
        Getter of the gender

        :return: An integer containing the gender
        """
        return self.__gender

    def set_gender(self, gender: int):
        """
        Setter of the gender

        :param gender: An integer containing the gender
        """
        self.__gender = gender

    def get_handedness(self) -> int:
        """
        Getter of the handedness

        :return : An integer containing the handedness
        """
        return self.__handedness

    def set_handedness(self, handedness: int):
        """
        Setter of the handedness

        :param handedness: An integer containing the handedness
        """
        self.__handedness = handedness

    def get_test_image(self) -> bytes:
        """
        Getter of the test_image

        :return: An test_image object
        """
        return self.__test_image

    def set_test_image(self, test_image: bytes):
        """
        Setter of the test_image

        :param test_image: An test_image object
        """
        self.__test_image = test_image

    def get_test_image_id(self) -> int:
        """
        Getter of the test_image_id

        :return : An integer containing the test_image_id
        """
        return self.__test_image_id

    def set_test_image_id(self, test_image_id: int):
        """
        Setter of the test_image_id

        :param test_image_id: An integer containing the test_image_id
        """
        self.__test_image = test_image_id
