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


class ComparWithStrError(InterpretException2):

    def modify_mess(self, operator='',operand0='',operand1=''):
        ComparWithStrError.message = {
            'win32': f"Error using {operator}\nComparison between {operand0} and {operand1} is not supported."
        }


# windows平台此处message过长，出现180列换行问题，需要修改
class ErrorUsingMul(InterpretException2):
    message = {
        'win32': "Error using *\nIncorrect dimensions for matrix multiplication. Check that the number of columns in the first matrix matches the number of rows in the second matrix. To perform elementwise multiplication, use '.*'.\n"
    }


class ErrorUsingRighDiv(InterpretException2):
    message = {
        'win32': "Error using /\nArguments must be numeric, char, or logical.\n"
    }


class ErrorUsingleftDiv(InterpretException2):
    message = {
        'win32': "Error using \\\nArguments must be numeric, char, or logical.\n"
    }


