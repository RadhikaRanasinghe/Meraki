from TestImage import TestImage


class User:
    def __init__(self, test_image: TestImage, age: int, gender: int, handedness: int):
        """This is the constructor

        :param test_image : TestImage object
        :param age : age of the user
        :param gender : gender of the user
        :param handedness : handedness of the user
        """

        self.__test_image: TestImage = test_image
        self.__age: int = age
        self.__gender: int = gender
        self.__handedness: int = handedness

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

       :return:  An integer containing the gender
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

        :return: An integer containing hte handedness
        """
        return self.__handedness

    def set_handedness(self, handedness: int):
        """
        Setter of the handedness

        :param handedness: An integer containing the handedness
        """
        self.__handedness = handedness

    def get_test_image(self) -> TestImage:
        """
        Getter of the test_image

        :return: A TestImage type object
        """
        return self.__test_image

    def set_test_image(self, test_image: TestImage):
        """
        Setter of the test_image

        :param test_image: A TestImage type object
        """
        self.__test_image = test_image