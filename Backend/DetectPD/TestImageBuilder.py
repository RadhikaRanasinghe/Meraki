from TestImage import TestImage


class TestImageBuilder(object):
    """
    This class is used as the builder class to take the values of the features of the image taken for the test.

     Attributes:
         __rms (float): Root Mean Square
         __max_between_st_ht (float): The maximum difference between ST (Stencil Trace) and HT(Handwritten Trace) radius
         __min_between_st_ht (float): The minimum difference between ST and HT radius
         __std_deviation_st_ht (float): Standard deviation of the difference between ST and HT radius
         __mrt (float): Mean Relative Tremor
         __max_ht (float): Maximum HT (Handwritten Trace) radius
         __min_ht (float): Minimum HT (Handwritten Trace) radius
         __std_ht (float): Standard deviation of the HT (Handwritten Trace) radius
         __changes_from_negative_to_positive_between_st_ht (float): the number of times the difference between ST and HT
         radius changes from negative to positive, or vice-versa

    """
    __rms: float = None
    __max_between_st_ht: float = None
    __min_between_st_ht: float = None
    __std_deviation_st_ht: float = None
    __mrt: float = None
    __max_ht: float = None
    __min_ht: float = None
    __std_ht: float = None
    __changes_from_negative_to_positive_between_st_ht: float = None

    def __init__(self):
        pass

    def build(self) -> TestImage:
        test_image = TestImage()

        test_image.set_rms(self.__rms)
        test_image.set_max_between_st_ht(self.__max_between_st_ht)
        test_image.set_min_between_st_ht(self.__min_between_st_ht)
        test_image.set_std_deviation_st_ht(self.__std_deviation_st_ht)
        test_image.set_mrt(self.__mrt)
        test_image.set_max_ht(self.__max_ht)
        test_image.set_min_ht(self.__min_ht)
        test_image.set_std_ht(self.__std_ht)
        test_image.set_changes_from_negative_to_positive_between_st_ht(
            self.__changes_from_negative_to_positive_between_st_ht
        )

        return test_image

    def get_rms(self) -> float:
        """
        Getter of the Root Mean Square (RMS) of the TestImage

        :return: A float containing the Root Mean Square
        """
        return self.__rms

    def set_rms(self, rms: float):
        """
        Setter of the Root Mean Square (RMS) of the TestImage

        :param rms: A float containing the RMS
        """
        self.__rms = rms
        return self

    def get_max_between_st_ht(self) -> float:
        """
        Getter of the maximum difference between ST (stencil Trace)
        and HT (Handwritten Trace) radius of the TestImage

        :return: A float containing the maximum difference between ST and HT
        """
        return self.__max_between_st_ht

    def set_max_between_st_ht(self, max_between_st_ht: float):
        """
        Setter of the maximum difference between ST (Stencil Trace)
        and HT (Handwritten Trace) radius of the TestImage.

        :param max_between_st_ht: A float containing the maximum difference between ST and HT
        """
        self.__max_between_st_ht = max_between_st_ht
        return self

    def get_min_between_st_ht(self) -> float:
        """
        Getter of the minimum difference between ST (Stencil Trace) and
        HT (Handwritten Trace) radius of the TestImage.

        :return: A float containing the minimum difference between ST and HT
        """
        return self.__min_between_st_ht

    def set_min_between_st_ht(self, min_between_st_ht: float):
        """
         Setter of the minimum difference between ST (Stencil Trace) and
         HT (Handwritten Trace) radius of the TestImage.

         :param min_between_st_ht: A float containing the minimum difference between ST and HT
         """
        self.__min_between_st_ht = min_between_st_ht
        return self

    def get_std_deviation_st_ht(self) -> float:
        """
        Getter of the standard deviation of the difference between ST (Stencil Trace) and
        HT (Handwritten Trace) radius of the TestImage.

        :return: A float containing standard deviation of the difference between ST and HT
        """
        return self.__std_deviation_st_ht

    def set_std_deviation_st_ht(self, std_deviation_st_ht: float):
        """
        Setter of the standard deviation of the difference between ST (Stencil Trace) and
        HT (Handwritten Trace) radius of the TestImage.

        :param std_deviation_st_ht: A float containing standard deviation of the difference between ST and HT
        """
        self.__std_deviation_st_ht = std_deviation_st_ht
        return self

    def get_mrt(self) -> float:
        """
        Getter of the Mean Relative Tremor of the TestImage.

        :return: A float containing Mean Relative Tremor
        """
        return self.__mrt

    def set_mrt(self, mrt):
        """
        Setter of the Mean Relative Tremor of the TestImage.

        :param mrt: A float containing Mean Relative Tremor
        """
        self.__mrt = mrt
        return self

    def get_max_ht(self) -> float:
        """
        Getter of the Maximum HT (Handwritten Trace) radius of the TestImage.

        :return: A float containing Maximum HT radius
        """
        return self.__max_ht

    def set_max_ht(self, max_ht: float):
        """
        Setter of the Maximum HT (Handwritten Trace) radius of the TestImage.

        :param max_ht: A float containing Maximum HT radius
        """
        self.__max_ht = max_ht
        return self

    def get_min_ht(self) -> float:
        """
        Getter of the Minimum HT (Handwritten Trace) radius of the TestImage.

        :return: A float containing Minimum HT radius
        """
        return self.__min_ht

    def set_min_ht(self, min_ht: float):
        """
        Setter of the Minimum HT (Handwritten Trace) radius of the TestImage.

        :param min_ht: A float containing Minimum HT radius
        """
        self.__min_ht = min_ht
        return self

    def get_std_ht(self) -> float:
        """
        Getter of the standard deviation of the HT (Handwritten Trace) radius of the TestImage.

        :return: A float containing standard deviation of the HT radius
        """
        return self.__std_ht

    def set_std_ht(self, std_ht: float):
        """
        Setter of the standard deviation of the HT (Handwritten Trace) radius of the TestImage.

        :param std_ht: A float containing standard deviation of the HT radius
        """
        self.__std_ht = std_ht
        return self

    def get_changes_from_negative_to_positive_between_st_ht(self) -> float:
        """
        Getter of the number of times the difference between ST (Stencil Trace) and HT (Handwritten Trace)
        radius changes from negative to positive, or vice-versa of the TestImage.

        :return: A float containing the number of times the difference between ST and HT
        radius changes from negative to positive, or vice-versa
        """
        return self.__changes_from_negative_to_positive_between_st_ht

    def set_changes_from_negative_to_positive_between_st_ht(self, change: float):
        """
        Setter of the number of times the difference between ST (Stencil Trace) and HT (Handwritten Trace)
        radius changes from negative to positive, or vice-versa of the TestImage.

        :param change: A float containing the number of times the difference between ST and HT
        radius changes from negative to positive, or vice-versa
        """
        self.__changes_from_negative_to_positive_between_st_ht = change
        return self
