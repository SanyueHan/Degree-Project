from enum import Enum


# Abstract Syntax Tree Node Type
class ASTNodeType(Enum):
    PROGRAM = "Program"

    # Statements
    DCL_STMT = "Declaration Statement"
    ASS_STMT = "Assignment Statement"
    EXP_STMT = "Expression Statement"

    # Expressions
    OR_EXP = "Logic OR Expression"
    AND_EXP = "Logic AND Expression"
    EQ_EXP = "Equal Expression"
    REL_EXP = "Relation Expression"
    ADD_EXP = "Additive Expression"
    MUL_EXP = "Multiplicative Expression"
    PRI_EXP = "Primary Expression"

    # Literals
    NUM_LIT = "Number Literal"

    ID = "Identifier"
