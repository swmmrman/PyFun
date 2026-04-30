class cypher:
    def __init__(self):
        self.ALPHA = "ABCDEFGHIJKLMNOPQRSTUVWXYZ ,.\"')(=:"
        self.key = "ABCDEFGHIJKLMNOPQRSTUVWXYZ ,.\"')(=:"
        self.text = ""

    def decrypt(self) -> str:
        return self.text

    def update(self, a, b):
        self.old_key = self.key

    def revert(self):
        self.key = self.old_key

    self.add_text(self, text):
        self.text += text
