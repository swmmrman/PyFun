class cypher:
    def __init__(self, text=""):
        self.ALPHA = "ABCDEFGHIJKLMNOPQRSTUVWXYZ ,.\"')(=:"
        self.key = "ABCDEFGHIJKLMNOPQRSTUVWXYZ ,.\"')(=:"
        #self.key = "kxvmcnophqrszyijadlegwbuft ,.\"')(=:"
        if len(text) > 0:
            self.text = text
        self.old_key = ""

    def decrypt(self) -> str:
        outstring = ""
        for char in self.text:
            if char == "\n":
                outstring += "\n"
            else:
                outstring += self.key[self.ALPHA.find(char.upper())]
        return outstring

    def update(self, a, b):
        self.old_key = self.key
        index = self.ALPHA.find(a.upper())
        self.key[index] = b

    def revert(self):
        self.key = self.old_key

    def add_text(self, text):
        self.text += text

    def load_temp(self):
        with open('cyphers.txt', "r") as file:
            self.text = file.read()
