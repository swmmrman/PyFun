class cypher:
    def __init__(self, text=""):
        self.ALPHA = "ABCDEFGHIJKLMNOPQRSTUVWXYZ ,.\"')(=:"
        self.key = "ABCDEFGHIJKLMNOPQRSTUVWXYZ ,.\"')(=:"
        #self.key = "kxvmcnophqrszyijadlegwbuft ,.\"')(=:"
        if len(text) > 0:
            self.text = text
        self.old_key = ""

    def decrypt(self) -> str:
        return self.text

    def update(self, a, b):
        self.old_key = self.key
        index = self.ALPHA.find(a.upper())
        self.key[index] = b

    def revert(self):
        self.key = self.old_key

    def add_text(self, text):
        self.text += text
