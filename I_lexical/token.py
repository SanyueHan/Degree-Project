class Token:
    def __init__(self, t_type=None, t_text=None):
        self.type = t_type
        self.text = t_text
        # todo: row/col

    def __repr__(self):
        return f"type: {self.type}, value: {self.text}"

    def get_type(self):
        return self.type

    def get_text(self):
        return self.text
