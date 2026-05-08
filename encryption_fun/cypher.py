from pathlib import Path

A_Z_ALPHA = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


class cypher:
    def __init__(self, text="", file="ciphers.txt"):
        self.ALPHA = "ABCDEFGHIJKLMNOPQRSTUVWXYZ !,.\"')(=:?"
        self.key = "ABCDEFGHIJKLMNOPQRSTUVWXYZ !,.\"')(=:?"
        # self.key = "kxvmcnophqrszyijadlegwbuft !,.\"')(=:?"
        self.old_key = ""
        self.decrypted_text = ""
        self.text = ""
        if len(text) > 0:
            self.add_text(text)
        else:
            self.load_file(file)

        self.decrypted_offsets = []
        self.last_decrypted_offsets = 1

    def add_text(self, text: str):
        self.text += text
        self.reset()

    def add_text_block(self):
        self.text = ""
        print("Paste content.  CRTL-D to end")
        inputing = True
        in_text = ""
        while inputing:
            new_line = ""
            try:
                new_line = input()
            except EOFError:
                inputing = False

            in_text += new_line + "\n"

        self.text = in_text
        self.reset()

    def ceaser_check(self) -> dict:
        possible_offsets = {}
        for i in self.decrypted_offsets:
            occurences = self.decrypted_offsets.count(i)
            if occurences >= 3:
                possible_offsets.update({i: occurences})
        return possible_offsets

    ### shift is the ceaser shift

    def ceaser_decrypt(self, shift: int) -> str:
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

    def clear_text(self):
        self.text = ""
        self.reset()

    def count_chars(self):
        print("Character counts:")
        upper_text = self.text.upper()
        counts = {}
        for char in A_Z_ALPHA:
            count = upper_text.count(char)
            counts[char] = count

        sorted_counts = dict(reversed(sorted(counts.items(), key=lambda item: item[1])))
        for key in sorted_counts:
            print(f"{sorted_counts[key]}:{key} ", end="")

        print("")

    def decrypt(self) -> str:
        """
        Uses the current key to try decrypt the cipher text\n
        Characters that are not decrypted print in uppercase\n
        Returns as a string.  To print use print_decrypted
        """
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

    def load_file(self, name: str):
        with open(name, "r") as file:
            self.text = file.read()
            self.decrypted_text = self.decrypt()

    def multi_update(self, a: str, b: str):
        """Update multiple characters at once.  Strings must be mathching length"""
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

    def print_decrypted(self):
        """Prints the decrypted cipher to console"""
        print(self.decrypted_text)

    def print_text(self):
        """Print the original cipher text"""
        print(self.text)

    def reset(self):
        """reset everything but the original cipher"""
        self.key = self.ALPHA
        self.decrypted_text = self.decrypt()
        self.decrypted_offsets = []

    def revert(self):
        """
        Revert the last character update.\n
        Also removes the last entry to offsets\n
        Then reruns decrypt to fix self.decrypted_text\n
        Can only undo the last one.
        """
        if self.old_key == "":
            print("No reverts available")
            return

        self.key = self.old_key
        self.old_key = ""
        for _ in range(0, self.last_decrypted_offsets):
            self.decrypted_offsets.pop(-1)

        self.last_decrypted_offsets = 0
        self.decrypted_text = self.decrypt()

    def revert_letter(self, letter: str, one: bool = True):
        """Revert any letter.\n
        If one is not set or true.  It will revert just the first one found in the key.\n
        If false, it will reset all instances in the key.
        """
        self.old = self.key
        index = self.key.find(letter)
        count = 1
        if not one:
            count = -1

        self.key = self.key.replace(letter, self.ALPHA[index], count)

    def save(self, outfile_name: str):
        """
        Save the current cipher text.\n
        """
        p = Path(outfile_name)
        if p.exists():
            resp = input("File exists: Overwrite y/[n]").lower()
            if resp != "y":
                return
        with open(outfile_name, "w") as file:
            file.write(self.text)

    def save_decrypted(self, outfile_name: str):
        """
        Save the current decrypted text\n
        """
        if Path(outfile_name).exists:
            resp = input("File exists: Overwrite y/[n]").lower()
            if resp != "y":
                return
        with open(outfile_name, "w") as file:
            file.write(self.decrypted_text)

    def update(self, a: str, b: str):
        self.old_key = self.key
        self.decrypted_offsets.append(
            A_Z_ALPHA.find(a.upper()) - A_Z_ALPHA.find(b.upper())
        )
        self.last_decrypted_offsets = 1
        self.key = self.key.replace(a.upper(), b)
        self.decrypted_text = self.decrypt()


def atbash_encrypt(text: str, key: str):
    outstring = ""
    for char in text:
        case = char.isupper()
        index = A_Z_ALPHA.find(char.upper())
        new_char = key[index] if index >= 0 else char
        if not case:
            new_char = new_char.lower()

        outstring += new_char
    return outstring


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
