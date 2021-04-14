import os


def read_from(path):
    with open(path, "r") as file:
        string = file.read()
    return string


def python_execute_output(path):
    # working directory is Degree-Project/test_interpreter, so relative path is ../MATLAB.py
    os.system(f"python3 ../MATLAB.py {path} > temp.txt")
    result = read_from("temp.txt")
    os.system("rm temp.txt")
    return result


def test_method_builder(path, matlab_execute_output, python_execute_output):
    target_output = matlab_execute_output(path)
    actual_output = python_execute_output(path)

    def method(self):
        self.assertEqual(target_output, actual_output)
    return method
