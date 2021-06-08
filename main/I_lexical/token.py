class Token:
    def __init__(self, t_type=None, t_text=None, row=None, col=None):
        self.type = t_type
        self.text = t_text
        self.row = row
        self.col = col

    def __str__(self):
        return self.text

    def __repr__(self):
        return '        '.join([
            f"row = {self.row:>3}",
            f"col = {self.col:>3}",
            f"type = {str(self.type)[10:]:<10}",
            f"text = {repr(self.text)}"
        ])

    def get_type(self):
        return self.type

    def get_text(self):
        return self.text

    def get_line(self):
        return self.row


class TokenListPrinter:
    @staticmethod
    def print(token_list):
        for t in token_list:
            print(repr(t))
