#!/usr/bin/env python
import sys

import cypher


def print_help():
    str = """
Usage: x=y or command.  x=y to replace a lettter(s)
Commands
Command      Shortcut
add_block    ab         add a text block, replacing old cipher text
add_text     at         add text to the existing cipher
ceaser [i]   cd [i]     Attempt ceaser decrypt [i] is the shift
clear_text   ct         Empty the current cipher and reset state
count        cc         Get a list of character counts
multi        m a b      update multiple at the same time.
offsets                 Print the current offsets
print        p          Print the current decrypted text
print_key    pk         Print the current key
^_sorted     pks        Print the key sorted
print_text   pt         Print the original cipher text
quit         q          quit
reset                   Reset the cipher.
revert       r          Undo the last operation.
save [x]     s [x]      Save cipher to file [x]
^_decrypted  sd [name]  Same as save, but current clear text
update       u a b      Update the a = Encypted leter, b = decrypted
help         h          Print this message
"""
    print(str)


def run_command(input, cypher: cypher.cypher):
    global running
    parts = input.split(" ")
    command = parts[0].lower()
    eq_sign = command.find("=")
    if eq_sign > 0:
        parts += command.split("=")
        if len(parts[0]) > 1 or len(parts[1] > 1):
            command = "m"
        else:
            command = "u"
    match command:
        case "add_block" | "ab":
            c.add_text_block()

        case "ceaser" | "cd":
            if len(parts) < 2:
                print("Missing shift")
                return
            print(c.ceaser_decrypt(int(parts[1])))

        case "clear_text" | "ct":
            c.clear_text()

        case "count" | "cc":
            c.count_chars()

        case "add_text" | "at":
            c.add_text(" ".join(parts[1:]))

        case "mutli" | "m":
            if len(parts) < 3:
                print("Missing opperand")
                return
            cypher.multi_update(parts[1], parts[2])
            check = cypher.ceaser_check()
            if check != {}:
                print(f"Possible Ceaser cipher {check}")

        case "offsets":
            print(c.decrypted_offsets)

        case "print" | "p":
            cypher.print_decrypted()

        case "print_key" | "pk":
            print(c.key)

        case "print_key_sorted" | "pks":
            print("".join(sorted(c.key)))

        case "print_text" | "pt":
            c.print_text()

        case "quit" | "q":
            print("goodbye")
            running = False

        case "revert" | "r":
            c.revert()

        case "reset":
            c.reset()
            c.print_decrypted()

        case "save" | "s":
            c.save(parts[1])

        case "save_decrypted" | "sd":
            c.save_decrypted(parts[1])

        case "update" | "u":
            if len(parts) < 3:
                print("Missing opperand")
                return
            cypher.update(parts[1], parts[2])
            check = cypher.ceaser_check()
            if check != {}:
                print(f"Possible Ceaser cipher {check}")

        case "help" | "h":
            print_help()

        case _:
            print(f"{command} not recognized. h or help to print help")


cipher = ""
if not sys.stdin.isatty():
    for line in sys.stdin:
        cipher += line
    old_stdin = sys.stdin
    sys.stdin = open("/dev/tty")
    c = cypher.cypher(text=cipher)
else:
    print("File to read from: [ciphers.txt]")
    ans = input()
    if ans == "":
        c = cypher.cypher()
    else:
        c = cypher.cypher(file=ans)

c.print_decrypted()

running = True
while running:
    command = input("Command:")
    run_command(command, c)
