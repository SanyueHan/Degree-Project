"""
https://ww2.mathworks.cn/help/matlab/matrices-and-arrays.html?s_tid=CRUX_lftnav
"""
import random


DIRECTORY = '../../test_cases/language_fundamentals/ii_matrices_and_arrays/'
REPETITION = 100


def random_array():
    return "[" + ''.join(" "*random.randint(0, 2)+random.choice("+-")+random.choice("123456789")
                         for _ in range(random.randint(5, 10))) + "]\n"


if __name__ == '__main__':
    with open(DIRECTORY+'test_array_construction.m', "w") as file:
        for i in range(REPETITION):
            file.write(random_array())
