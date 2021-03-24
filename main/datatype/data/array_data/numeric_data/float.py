from main.datatype.classes import DataClass
from main.datatype.data.array_data.numeric import Numeric


class Float(Numeric):
    Class = DataClass.FLOAT

    def __str__(self):
        if all((int(i) == i) for i in self):
            max_len = max(len(str(int(i))) for i in self)
            if max_len <= 3:
                return self.to_string(self.__show, width=6, precision=0)
            elif max_len <= 8:
                return self.to_string(self.__show, width=12, precision=0)
        return self.to_string(self.__show)
        # todo: scientific notation for too big or too small

    @staticmethod
    def __show(item, width=10, precision=4):
        return f"{item:>{width}.{precision}f}"
