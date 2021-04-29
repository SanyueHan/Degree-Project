import os
import re
import time


REMOVE = re.compile(".\b|\b|Error: ")


def read_from(path):
    with open(path, "r") as file:
        string = file.read()
    return string


def python_execute(path):
    # working directory is Degree-Project/test_interpreter, so relative path is ../MATLAB.py
    command = f"python3 ../MATLAB.py {path} > {path[:-2]}_python.txt"
    print(command)
    os.system(command)
    result = read_from(f"{path[:-2]}_python.txt")
    os.system(f"rm {path[:-2]}_python.txt")
    return result


def matlab_execute(path, error=False):
    command = f"matlab -nodisplay -nosplash -nodesktop -r \"run('{path}'); exit;\" -logfile {path[:-2]}_matlab.txt"
    if error:
        # adding a & at the end of the command to cancel blocking the unittest process
        command += " &"
    print(command)
    os.system(command)
    if error:
        # wait for the matlab software process finish its running and error reporting
        time.sleep(10)
    result = read_from(f"{path[:-2]}_matlab.txt")
    os.system(f"rm {path[:-2]}_matlab.txt")

    if error:
        # cancel the backspace character along with the character behind it (if exist)
        result = re.sub(REMOVE, '', result)

    if error:
        # remove licenses information and matlab program stack information
        return "\n".join(result.split("\n")[10:-5])
    return "\n".join(result.split("\n")[10:])


def test_method_builder(target, actual):
    def method(self):
        self.assertEqual(target, actual)
    return method


def package_test_class(class_name, directory, error=False):
    for test_case in os.listdir(directory):
        if test_case[-1] == 'm':
            matlab_result = matlab_execute(directory + test_case, error=error)
            python_result = python_execute(directory + test_case)
            test_method = test_method_builder(matlab_result, python_result)
            setattr(class_name, test_case, test_method)
