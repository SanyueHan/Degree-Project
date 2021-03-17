from enum import Enum


# Abstract Syntax Tree Node Type
class ASTNodeType(Enum):
    # Program
    STMT_LIST = "STATEMENT LIST"

    # Statements
    ASS_STMT = "ASSIGNMENT STATEMENT"
    EXP_STMT = "EXPRESSION STATEMENT"
    CLR_STMT = "CLEAR STATEMENT"
    SEL_STMT = "SELECTION STATEMENT"
    ITR_STMT = "ITERATION STATEMENT"
    JMP_STMT = "JUMP STATEMENT"

    # Statement Components
    EO_STMT = "END OF STATEMENT"
    ID_LIST = "IDENTIFIER LIST"
    SEL_ClS = "SELECTION CLAUSE"
    FOR_CLS = "FOR CLAUSE"
    WHL_CLS = "WHILE CLAUSE"

    # Expressions
    ASS_EXP = "ASSIGNMENT EXPRESSION"
    LOR_EXP = "LOGIC OR EXPRESSION"
    LAN_EXP = "LOGIC AND EXPRESSION"
    EQL_EXP = "EQUAL EXPRESSION"
    REL_EXP = "RELATIONAL EXPRESSION"
    ADD_EXP = "ADDITIVE EXPRESSION"
    MUL_EXP = "MULTIPLICATIVE EXPRESSION"
    UNY_EXP = "UNARY EXPRESSION"
    PRI_EXP = "PRIMARY EXPRESSION"

    # Literals
    NUM_LIT = "NUMBER LITERAL"
    STR_LIT = "STRING LITERAL"

    ID = "IDENTIFIER"
