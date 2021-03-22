from main.datatype.classes import DataClass
from main.datatype.data.array_data.numeric import Numeric


class Float(Numeric):
    Class = DataClass.FLOAT

    def __str__(self):
        if all(self.__is_whole(i) for i in self):
            max_len = max(len(str(self.__whole(i))) for i in self)
            if max_len <= 3:
                return self.to_string(self.__show_as_whole, space=6)
            elif max_len <= 8:
                return self.to_string(self.__show_as_whole, space=12)
        return self.to_string(self.__show_as_float)
        # todo: scientific notation for too big or too small

    @staticmethod
    def __is_whole(item):
        return int(item) == item

    @staticmethod
    def __whole(item):
        return int(item)

    @staticmethod
    def __show_as_whole(item, space=6):
        string = str(int(item))
        vacancy = space - len(string)
        return " " * vacancy + string

    @staticmethod
    def __show_as_float(item):
        string = f"{item:.4f}"
        vacancy = 10 - len(string)
        return " " * vacancy + string
