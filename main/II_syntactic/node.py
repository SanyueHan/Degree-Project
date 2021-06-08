# Abstract Syntax Tree Node
class ASTNode:
    def __init__(self, n_type=None, n_text=None, n_line=0, children=None):
        self.type = n_type
        self.text = n_text
        self.line = n_line
        self.children = children if children else []

    def get_type(self):
        return self.type

    def get_text(self):
        return self.text

    def get_line(self):
        return self.line

    def get_children(self):
        return self.children

    def num_children(self):
        return len(self.children)

    def add_child(self, child):
        self.children.append(child)

    def get_child(self, index=0):
        return self.children[index]

    def dump(self, indent=0):
        print(f"{' '*indent}{self.get_type()} {self.get_text()}")
        for child in self.children:
            child.dump(indent+4)

    def __str__(self):
        return f"{str(self.type)[12:]}: {repr(self.text)}"


class ASTTreePrinter:
    def __init__(self):
        self.vec_left = [0 for _ in range(100)]

    def print(self, node):
        print()
        self.display(node)
        print()

    def display(self, node, indent=0):
        if indent > 0:
            print("  ", end="")
            for i in range(indent - 1):
                print("│     " if self.vec_left[i] else "      ", end="")
            print("├── " if self.vec_left[indent - 1] else "└── ", end="")

        if not node:
            print("(null)")
            return None

        print(node)
        if node.num_children() == 0:
            return None

        children = node.get_children()
        self.vec_left[indent] = 1
        for child in children[:-1]:
            self.display(child, indent + 1)
        self.vec_left[indent] = 0
        self.display(children[-1], indent + 1)
