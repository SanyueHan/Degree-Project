class Token:
    def __init__(self, t_type=None, t_text=None, row=None, col=None):
        self.type = t_type
        self.text = t_text
        self.row = row
        self.col = col

    def __repr__(self):
        return f"type: {self.type}, text: {self.text}, row={self.row}, col={self.col}"

    def get_type(self):
        return self.type

    def get_text(self):
        return self.text
