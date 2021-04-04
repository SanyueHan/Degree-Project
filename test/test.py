import unittest
import os

INPUT_DIR = "designed_input/"
OUTPUT_DIR = "desired_output/"


class TestInterpreterIntegration(unittest.TestCase):
    pass


def script_execute_output(path):
    # working directory is Degree-Project/test, so relative path is ../MATLAB.py
    os.system(f"python3 ../MATLAB.py {path} > temp.txt")
    result = read_from("temp.txt")
    os.system("rm temp.txt")
    return result


def read_from(path):
    with open(path, "r") as file:
        string = file.read()
    return string


def test_method_builder(filename):
    actual_output = script_execute_output(INPUT_DIR + filename)
    desired_output = read_from(OUTPUT_DIR + filename[:-2] + ".txt")

    def method(self):
        self.assertEqual(desired_output, actual_output)
    return method


for test_case in os.listdir(INPUT_DIR):
    test_method = test_method_builder(test_case)
    setattr(TestInterpreterIntegration, test_case, test_method)


if __name__ == '__main__':
    unittest.main()
