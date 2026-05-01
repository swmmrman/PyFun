class cypher:
    A_Z_ALPHA = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    def __init__(self, text="", file="cyphers.txt"):
        self.ALPHA = "ABCDEFGHIJKLMNOPQRSTUVWXYZ !,.\"')(=:?"
        self.key = "ABCDEFGHIJKLMNOPQRSTUVWXYZ !,.\"')(=:?"
        # self.key = "kxvmcnophqrszyijadlegwbuft !,.\"')(=:?"
        if len(text) > 0:
            self.text = text
        self.old_key = ""
        self.decrypted_text = ""
        self.load_file(file)
        self.decrypted_offsets = []

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
        self.decrypted_offsets.append(
            cypher.A_Z_ALPHA.find(a.upper()) - cypher.A_Z_ALPHA.find(b.upper())
        )
        self.key = self.key.replace(a.upper(), b)
        self.decrypted_text = self.decrypt()

    def revert(self):
        self.key = self.old_key
        self.decrypted_offsets.pop(-1)

    def revert_letter(self, letter, one=True):
        self.old = self.key
        index = self.key.find(letter)
        count = 1
        if not one:
            count = -1
        self.key = self.key.replace(letter, self.ALPHA[index], count)

    def add_text(self, text):
        self.text += text

    def load_file(self, file):
        with open(file, "r") as file:
            self.text = file.read()
            self.decrypted_text = self.decrypt()


#    def ceaser_check(self):
