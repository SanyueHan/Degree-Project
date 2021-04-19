import unittest
import os
from utils import test_method_builder, python_execute, matlab_execute


I_LEXICAL_ERROR = "test_cases/error_handling/i_lexical_error/"


class TestLexicalError(unittest.TestCase):
    pass


for test_case in os.listdir(I_LEXICAL_ERROR):
    python_result = python_execute(I_LEXICAL_ERROR + test_case)
    matlab_result = matlab_execute(I_LEXICAL_ERROR + test_case, error=True)
    test_method = test_method_builder(python_result, matlab_result)
    setattr(TestLexicalError, test_case, test_method)
