A_Z_ALPHA = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


class cypher:
    def __init__(self, text="", file="ciphers.txt"):
        self.ALPHA = "ABCDEFGHIJKLMNOPQRSTUVWXYZ !,.\"')(=:?"
        self.key = "ABCDEFGHIJKLMNOPQRSTUVWXYZ !,.\"')(=:?"
        # self.key = "kxvmcnophqrszyijadlegwbuft !,.\"')(=:?"
        self.old_key = ""
        self.decrypted_text = ""
        if len(text) > 0:
            self.text = text
        else:
            self.load_file(file)
        self.decrypted_offsets = []
        self.last_decrypted_offsets = 1

    def decrypt(self) -> str:
        outstring = ""
        for char in self.text:
            if char == "\n":
                outstring += "\n"
            elif char.upper() not in self.ALPHA:
                outstring += char
            else:
                if char.isupper():
                    outstring += self.key[self.ALPHA.find(char.upper())].upper()
                else:
                    outstring += self.key[self.ALPHA.find(char.upper())]
        return outstring

    def print_decrypted(self):
        print(self.decrypted_text)

    def update(self, a, b):
        self.old_key = self.key
        self.decrypted_offsets.append(
            A_Z_ALPHA.find(a.upper()) - A_Z_ALPHA.find(b.upper())
        )
        self.last_decrypted_offsets = 1
        self.key = self.key.replace(a.upper(), b)
        self.decrypted_text = self.decrypt()

    def multi_update(self, a, b):
        length = len(a)
        if len(b) != length:
            print("size of strings must match")
            return
        self.old_key = self.key
        self.last_decrypted_offsets = 0
        for i in range(0, length):
            offset = A_Z_ALPHA.find(a[i].upper()) - A_Z_ALPHA.find(b[i].upper())
            self.decrypted_offsets.append(offset)
            self.last_decrypted_offsets += 1
            self.key = self.key.replace(a[i].upper(), b[i])
            self.decrypted_text = self.decrypt()

    def revert(self):
        if self.old_key == "":
            print("No reverts available")
            return
        self.key = self.old_key
        self.old_key = ""
        for _ in range(0, self.last_decrypted_offsets):
            self.decrypted_offsets.pop(-1)
        self.last_decrypted_offsets = 0
        self.decrypted_text = self.decrypt()

    def revert_letter(self, letter, one=True):
        self.old = self.key
        index = self.key.find(letter)
        count = 1
        if not one:
            count = -1
        self.key = self.key.replace(letter, self.ALPHA[index], count)

    def add_text(self, text):
        self.text += text
        self.reset()

    def clear_text(self):
        self.text = ""
        self.reset()

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
            if cap_char in A_Z_ALPHA:
                index = (A_Z_ALPHA.find(cap_char) + shift) % 26
                if char.isupper():
                    outstring += A_Z_ALPHA[index]
                else:
                    outstring += A_Z_ALPHA[index].lower()
            else:
                outstring += char
        return outstring

    def ceaser_check(self) -> dict:
        possible_offsets = {}
        for i in self.decrypted_offsets:
            occurences = self.decrypted_offsets.count(i)
            if occurences >= 3:
                possible_offsets.update({i: occurences})
        return possible_offsets

    def reset(self):
        self.key = self.ALPHA
        self.decrypted_text = self.decrypt()
        self.decrypted_offsets = []


def ceaser_encrypt(text: str, offset: int):
    outstring = ""
    for char in text:
        if char.upper() not in A_Z_ALPHA:
            outstring += char
            continue
        caps = char.isupper()
        index = (A_Z_ALPHA.find(char.upper()) + offset) % 26
        new_char = A_Z_ALPHA[index]
        if not caps:
            new_char = new_char.lower()
        outstring += new_char
    return outstring


def atbash_encrypt(text: str, key: str):
    outstring = ""
    for char in text:
        case = char.isupper()
        index = A_Z_ALPHA.find(char.upper())
        new_char = key[index] if index > 0 else char
        if not case:
            new_char = new_char.lower()
            outstring += new_char
    return outstring
