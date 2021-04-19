import os
import re
import time


PATTERN = re.compile(".\b|\b")


def read_from(path):
    with open(path, "r") as file:
        string = file.read()
    return string


def python_execute(path):
    # working directory is Degree-Project/test_interpreter, so relative path is ../MATLAB.py
    command = f"python3 ../MATLAB.py {path} > {path[-3]}_python.txt"
    print(command)
    os.system(command)
    result = read_from(f"{path[-3]}_python.txt")
    os.system(f"rm {path[-3]}_python.txt")
    return result


def matlab_execute(path, error=False):
    command = f"matlab -nodisplay -nosplash -nodesktop -r \"run('{path}'); exit;\" -logfile {path[-3]}_matlab.txt"
    if error:
        # adding a & at the end of the command to cancel blocking the unittest process
        command += " &"
    print(command)
    os.system(command)
    if error:
        # wait for the matlab software process finish its running and error reporting
        time.sleep(10)
    result = read_from(f"{path[-3]}_matlab.txt")
    os.system(f"rm {path[-3]}_matlab.txt")

    if error:
        # cancel the backspace character along with the character behind it (if exist)
        result = re.sub(PATTERN, '', result)

    if error:
        # remove licenses information and matlab program stack information
        return "\n".join(result.split("\n")[10:-5])
    return "\n".join(result.split("\n")[10:])


def test_method_builder(actual, target):
    def method(self):
        self.assertEqual(actual, target)
    return method
