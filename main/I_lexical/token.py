class Token:
    def __init__(self, t_type=None, t_text=None, row=None, col=None):
        self.type = t_type
        self.text = t_text
        self.row = row
        self.col = col

    def __str__(self):
        return self.text

    def get_type(self):
        return self.type

    def get_text(self):
        return self.text


if __name__ == "__main__":
    token = Token(t_text="test")
    print(str(token))
    print(token)
