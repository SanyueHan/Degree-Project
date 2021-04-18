import os


def read_from(path):
    with open(path, "r") as file:
        string = file.read()
    return string


def python_execute_output(path):
    # working directory is Degree-Project/test_interpreter, so relative path is ../MATLAB.py
    command = f"python3 ../MATLAB.py {path} > {path[-3]}_python.txt"
    print(command)
    os.system(command)
    result = read_from(f"{path[-3]}_python.txt")
    os.system(f"rm {path[-3]}_python.txt")
    return result


def test_method_builder(path, matlab, python):
    actual_output = python(path)
    target_output = matlab(path)

    def method(self):
        self.assertEqual(actual_output, target_output)
    return method
