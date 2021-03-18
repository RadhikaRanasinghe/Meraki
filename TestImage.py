class TestImage:
    __rms: float = None
    __max_between_st_ht: float = None
    __min_between_st_ht: float = None
    __std_deviation_st_ht: float = None
    __mrt: float = None
    __max_ht: float = None
    __min_ht: float = None
    __std_ht: float = None
    __changes_from_negative_to_positive_between_st_ht: float = None

    def get_rms(self) -> float:
        return self.__rms

    def set_rms(self, rms: float):
        self.__rms = rms

    def get_max_between_st_ht(self) -> float:
        return self.__max_between_st_ht

    def set_max_between_st_ht(self, max_between_st_ht: float):
        self.__max_between_st_ht = max_between_st_ht

    def get_min_between_st_ht(self) -> float:
        return self.__min_between_st_ht

    def set_min_between_st_ht(self, min_between_st_ht: float):
        self.__min_between_st_ht = min_between_st_ht

    def get_std_deviation_st_ht(self) -> float:
        return self.__std_deviation_st_ht

    def set_std_deviation_st_ht(self, std_deviation_st_ht: float):
        self.__std_deviation_st_ht = std_deviation_st_ht

    def get_mrt(self) -> float:
        return self.__mrt

    def set_mrt(self, mrt):
        self.__mrt = mrt

    def get_max_ht(self) -> float:
        return self.__max_ht

    def set_max_ht(self, max_ht: float):
        self.__max_ht = max_ht

    def get_min_ht(self) -> float:
        return self.__min_ht

    def set_min_ht(self, min_ht: float):
        self.__min_ht = min_ht

    def get_std_ht(self) -> float:
        return self.__std_ht

    def set_std_ht(self, std_ht: float):
        self.__std_ht = std_ht

    def get_changes_from_negative_to_positive_between_st_ht(self) -> float:
        return self.__changes_from_negative_to_positive_between_st_ht

    def set_changes_from_negative_to_positive_between_st_ht(self, change: float):
        self.__changes_from_negative_to_positive_between_st_ht = change
