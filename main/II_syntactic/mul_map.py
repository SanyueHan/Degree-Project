from main.II_syntactic.node_types import ASTNodeType

MUL_MAP = {
    '*': ASTNodeType.MML_EXP,
    '/': ASTNodeType.MRD_EXP,
    '\\': ASTNodeType.MRD_EXP,
    '.*': ASTNodeType.BSO_EXP,
    './': ASTNodeType.BSO_EXP,
    '.\\': ASTNodeType.BSO_EXP,
}
