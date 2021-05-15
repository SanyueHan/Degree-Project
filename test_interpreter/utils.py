import os
import re
import time


REDUNDANT_TEXT_1 = re.compile(r"[\s\S]*For online documentation, see https://www.mathworks.com/support\n"
                              "For product information, visit www.mathworks.com.\n \n")
REDUNDANT_TEXT_2 = re.compile(".\b|\b|Error: File:[ \n]")
REDUNDANT_TEXT_3 = re.compile(r"[\n]*Error in run[\s\S]*")


def read_from(path):
    with open(path, "r") as file:
        string = file.read()
    return string


def python_execute(path):
    temp = path[:-2] + "_python.txt"
    # working directory is Degree-Project/test_interpreter, so relative path is ../miniMATLAB.py
    command = f"python3 ../miniMATLAB.py {path} > {temp}"
    print(command)
    os.system(command)
    result = read_from(f"{temp}")
    os.system(f"rm {temp}")
    return result


def matlab_execute(path, error=False):
    temp = path[:-2] + "_matlab.txt"
    command = f"matlab -nodisplay -nosplash -nodesktop -nojvm -r \"run('{path}'); exit;\" -logfile {temp}"
    if error:
        # adding a & at the end of the command to cancel blocking the unittest process
        command += " &"
    print(command)
    os.system(command)
    if error:
        # wait for the matlab software process finish its running and error reporting
        time.sleep(10)
    result = read_from(f"{temp}")
    os.system(f"rm {temp}")

    # cancel license information (this information on windows is different with that on mac)
    result = re.sub(REDUNDANT_TEXT_1, '', result)
    # cancel the backspace character along with the character behind it (if exist)
    result = re.sub(REDUNDANT_TEXT_2, '', result)
    # cancel the stack information from matlab software
    result = re.sub(REDUNDANT_TEXT_3, '', result)

    return result


def test_method_builder(target, actual):
    def method(self):
        self.assertEqual(target, actual)
    return method


def package_test_class(class_name, error=False):
    for filename in os.listdir(class_name.directory):
        if filename[-1] == 'm':
            matlab_result = matlab_execute(class_name.directory + filename, error=error)
            python_result = python_execute(class_name.directory + filename)
            test_method = test_method_builder(matlab_result, python_result)
            setattr(class_name, filename, test_method)
