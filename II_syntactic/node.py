# Abstract Syntax Tree Node
class ASTNode:
    def __init__(self, n_type=None, n_text=None, n_stmt=False, children=None):
        self.type = n_type
        self.text = n_text
        self.stmt = n_stmt  # the argument deciding whether this is a statement or an expression
        self.children = children if children else []

    def get_type(self):
        return self.type

    def get_text(self):
        return self.text

    def get_stmt(self):
        return self.stmt

    def get_children(self):
        return self.children

    def add_child(self, child):
        self.children.append(child)

    def dump(self, indent=0):
        print(f"{' '*indent}{self.get_type()} {self.get_text()}")
        for child in self.children:
            child.dump(indent+4)
