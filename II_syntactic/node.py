# Abstract Syntax Tree Node
class ASTNode:
    def __init__(self, n_type=None, n_text=None, children=None):
        self.type = n_type
        self.text = n_text
        self.children = children if children else []

    def get_type(self):
        return self.type

    def get_text(self):
        return self.text

    def get_children(self):
        return self.children

    def num_children(self):
        return len(self.children)

    def add_child(self, child):
        self.children.append(child)

    def get_child(self, index):
        return self.children[index]

    def dump(self, indent=0):
        print(f"{' '*indent}{self.get_type()} {self.get_text()}")
        for child in self.children:
            child.dump(indent+4)
