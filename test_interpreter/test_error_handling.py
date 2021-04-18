import unittest
import os
import time
import re
from utils import read_from, test_method_builder, python_execute_output


LEXICAL_ERROR = "test_cases/error_handling/i_lexical_error/"
PATTERN = re.compile(".\b|\b")


def matlab_execute_output(path):
    # adding a & at the end of the command to cancel blocking the unittest process
    command = f"matlab -nodisplay -nosplash -nodesktop -r \"run('{path}'); exit;\" -logfile {path[-3]}_matlab.txt &"
    print(command)
    os.system(command)
    # wait for the matlab software process finish its running and error reporting
    time.sleep(10)
    result = read_from(f"{path[-3]}_matlab.txt")
    os.system(f"rm {path[-3]}_matlab.txt")
    # cancel the backspace character along with the character behind it (if exist)
    result = re.sub(PATTERN, '', result)
    # remove licenses information and matlab program stack information
    return "\n".join(result.split("\n")[10:-5])


class TestLexicalError(unittest.TestCase):
    pass


for test_case in os.listdir(LEXICAL_ERROR):
    test_method = test_method_builder(LEXICAL_ERROR + test_case, python_execute_output, matlab_execute_output)
    setattr(TestLexicalError, test_case, test_method)
