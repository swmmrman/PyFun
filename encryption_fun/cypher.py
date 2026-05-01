class cypher:
    A_Z_ALPHA = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    def __init__(self, text="", file="ceaser.txt"):
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

    ### shift is the ceaser shift
    def ceaser_decrypt(self, shift) -> str:
        shift = 0 - shift
        outstring = ""
        for char in self.text:
            cap_char = char.upper()
            if cap_char in cypher.A_Z_ALPHA:
                index = (cypher.A_Z_ALPHA.find(cap_char) + shift) % 26
                outstring += cypher.A_Z_ALPHA[index]
            else:
                outstring += char
        return outstring


    def ceaser_check(self):
