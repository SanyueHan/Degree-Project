import unittest
import os
from utils import read_from, test_method_builder, python_execute_output


REGULAR_USAGE = "test_cases/language_fundamentals/"


def matlab_execute_output(path):
    command = f"matlab -nodisplay -nosplash -nodesktop -r \"run('{path}'); exit;\" -logfile temp.txt"
    print(command)
    os.system(command)
    result = read_from("temp.txt")
    os.system("rm temp.txt")

    # remove licenses information
    return "\n".join(result.split("\n")[10:])


class TestRegularUsage(unittest.TestCase):
    pass


for test_case in os.listdir(REGULAR_USAGE):
    test_method = test_method_builder(REGULAR_USAGE + test_case, python_execute_output, matlab_execute_output)
    setattr(TestRegularUsage, test_case, test_method)


if __name__ == '__main__':
    unittest.main()
