from TestImage import TestImage


class TestImageBuilder(object):
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

    def build(self) -> object:
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
        return self.__rms

    def set_rms(self, rms: float) -> object:
        self.__rms = rms
        return self

    def get_max_between_st_ht(self) -> float:
        return self.__max_between_st_ht

    def set_max_between_st_ht(self, max_between_st_ht: float) -> object:
        self.__max_between_st_ht = max_between_st_ht
        return self

    def get_min_between_st_ht(self) -> float:
        return self.__min_between_st_ht

    def set_min_between_st_ht(self, min_between_st_ht: float) -> object:
        self.__min_between_st_ht = min_between_st_ht
        return self

    def get_std_deviation_st_ht(self) -> float:
        return self.__std_deviation_st_ht

    def set_std_deviation_st_ht(self, std_deviation_st_ht: float) -> object:
        self.__std_deviation_st_ht = std_deviation_st_ht
        return self

    def get_mrt(self) -> float:
        return self.__mrt

    def set_mrt(self, mrt) -> object:
        self.__mrt = mrt
        return self

    def get_max_ht(self) -> float:
        return self.__max_ht

    def set_max_ht(self, max_ht: float) -> object:
        self.__max_ht = max_ht
        return self

    def get_min_ht(self) -> float:
        return self.__min_ht

    def set_min_ht(self, min_ht: float) -> object:
        self.__min_ht = min_ht
        return self

    def get_std_ht(self) -> float:
        return self.__std_ht

    def set_std_ht(self, std_ht: float) -> object:
        self.__std_ht = std_ht
        return self

    def get_changes_from_negative_to_positive_between_st_ht(self) -> float:
        return self.__changes_from_negative_to_positive_between_st_ht

    def set_changes_from_negative_to_positive_between_st_ht(self, change: float) -> object:
        self.__changes_from_negative_to_positive_between_st_ht = change
        return self
