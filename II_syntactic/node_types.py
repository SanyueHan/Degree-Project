from enum import Enum


# Abstract Syntax Tree Node Type
class ASTNodeType(Enum):
    PROGRAM = "Program"

    # Statements
    DCL_STMT = "Declaration Statement"
    ASS_STMT = "Assignment Statement"
    EXP_STMT = "Expression Statement"

    # Expressions
    ADD_EXP = "Additive Expression"
    MUL_EXP = "Multiplicative Expression"
    PRI_EXP = "Primary Expression"

    # Literals
    NUM_LIT = "Number Literal"

    ID = "Identifier"
