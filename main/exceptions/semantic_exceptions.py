from main.exceptions.interpret_exception import InterpretException2


# 使用方式
# line=1
# filename="test1"
# error_statement='a=\"str\"'
# temp=UnaryOperatorForStrError(line,filename,error_statement)
# temp.modify_mess(op)
# return (a)
class UnaryOperatorForStrError(InterpretException2):

    def modify_mess(self, unary_operator=''):
        UnaryOperatorForStrError.message = {
            'win32': f"Unary operator '{unary_operator}' is not supported for operand of type 'string'.\n"
        }


class OperatorForStrError(InterpretException2):

    def modify_mess(self, operator=''):
        OperatorForStrError.message = {
            'win32': f"Operator '{operator}' is not supported for operands of type 'string'.\n"
        }


class CompareWithStrError(InterpretException2):

    def modify_mess(self, operator='', operand0='', operand1=''):
        CompareWithStrError.message = {
            'win32': f"Error using {operator}\nComparison between {operand0} and {operand1} is not supported.\n"
        }


class ErrorUsingDivision(InterpretException2):

    def modify_mess(self, operator=''):
        OperatorForStrError.message = {
            'win32': f"Error using {operator}\nArguments must be numeric, char, or logical.\n"  # 左除注意\\
        }


class UnrecognizedFunctionOrVar(InterpretException2):

    def modify_mess(self, identifier=''):
        UnrecognizedFunctionOrVar.message = {
            'win32': f"Unrecognized function or variable '{identifier}'.\n"
        }


class DimensionNotConsistentError(InterpretException2):

    def modify_mess(self, error_type=''):
        DimensionNotConsistentError.message = {
            'win32': f"Error using {error_type}\nDimensions of arrays being concatenated are not consistent.\n"
        }


# windows平台此处message过长，出现180列换行问题，需要修改
class ErrorUsingMultiply(InterpretException2):

    message = {
        'win32': "Error using *\nIncorrect dimensions for matrix multiplication. Check that the number of columns in the first matrix matches the number of rows in the second matrix. To perform elementwise multiplication, use '.*'.\n"
    }



