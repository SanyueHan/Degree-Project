from main.II_syntactic.node_types import ASTNodeType

MUL_OPERATOR_MAP = {
    '*': ASTNodeType.MML_EXP,
    '/': ASTNodeType.MRD_EXP,
    '\\': ASTNodeType.MRD_EXP,
    '.*': ASTNodeType.BSO_EXP,
    './': ASTNodeType.BSO_EXP,
    '.\\': ASTNodeType.BSO_EXP,
}

SEL_TERMINATOR_MAP = {
    'if': ('elseif', 'else', 'end'),
    'elseif': ('elseif', 'else', 'end'),
    'else': ('end', )
}
