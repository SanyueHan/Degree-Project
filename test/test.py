import unittest
import os

REGULAR_USAGE_CASES = "test_cases/regular_usage_cases/"


def python_execute_output(path):
    # working directory is Degree-Project/test, so relative path is ../MATLAB.py
    os.system(f"python3 ../MATLAB.py {path} > temp.txt")
    result = read_from("temp.txt")
    os.system("rm temp.txt")
    return result


def matlab_execute_output(path):
    command = f"matlab -nodisplay -nosplash -nodesktop -r \"run('{path}'); exit;\" -logfile temp.txt"
    print(command)
    os.system(command)
    result = read_from("temp.txt")
    os.system("rm temp.txt")
    return "\n".join(result.split("\n")[10:])


def read_from(path):
    with open(path, "r") as file:
        string = file.read()
    return string


def test_method_builder(filename):
    target_output = matlab_execute_output(REGULAR_USAGE_CASES + filename)
    actual_output = python_execute_output(REGULAR_USAGE_CASES + filename)

    def method(self):
        self.assertEqual(target_output, actual_output)
    return method


class TestRegularUsage(unittest.TestCase):
    pass


for test_case in os.listdir(REGULAR_USAGE_CASES):
    test_method = test_method_builder(test_case)
    setattr(TestRegularUsage, test_case, test_method)


if __name__ == '__main__':
    unittest.main()
