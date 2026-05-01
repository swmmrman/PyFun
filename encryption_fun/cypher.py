class cypher:
    def __init__(self, text=""):
        self.ALPHA = "ABCDEFGHIJKLMNOPQRSTUVWXYZ !,.\"')(=:"
        self.key = "ABCDEFGHIJKLMNOPQRSTUVWXYZ !,.\"')(=:"
        # self.key = "kxvmcnophqrszyijadlegwbuft !,.\"')(=:"
        if len(text) > 0:
            self.text = text
        self.old_key = ""
        self.decrypted_text = ""

    def decrypt(self) -> str:
        outstring = ""
        for char in self.text:
            if char == "\n":
                outstring += "\n"
            else:
                outstring += self.key[self.ALPHA.find(char.upper())]
        return outstring

    def print_decrypted(self):
        print(self.decrypted_text)

    def update(self, a, b):
        self.old_key = self.key
        self.key = self.key.replace(a.upper(), b)
        self.decrypted_text = self.decrypt()

    def revert(self):
        self.key = self.old_key

    def revert_letter(self, letter, one=True):
        self.old = self.key
        index = self.key.find(letter)
        count = 1
        if not one:
            count = -1
        self.key = self.key.replace(letter, self.ALPHA[index], count)

    def add_text(self, text):
        self.text += text

    def load_temp(self):
        with open("cyphers.txt", "r") as file:
            self.text = file.read()
            self.decrypted_text = self.decrypt()
