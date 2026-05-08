#!/usr/bin/env python
import sys

import cypher


def print_help():
    str = """
Usage: x=y or command.  x=y to replace a lettter(s)
Commands
Command    shortcut
print      p         Print the current decrypted text
print_key  pk        Print the current key
update     u a b     Update the a = Encypted leter, b = decrypted
multi      m a b     update multiple at the same time.
quit       q         quit
revert     r         Undo the last operation.
reset                Reset the cipher.
offsets              Print the current offsets
save [x]   s [x]     Save to file [x] save-decrypted to save the clear text
count      cc        Get a list of character counts
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
        case "add_text_block" | "atb":
            c.add_text_block()
        case "ceaser_decrypt" | "cd":
            if len(parts) < 2:
                print("Missing shift")
                return
            print(c.ceaser_decrypt(int(parts[1])))
        case "clear_text" | "ct":
            c.clear_text()
        case "count" | "cc":
            c.count_chars()
        case "load_text" | "lt":
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
            print(sorted(c.key))
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
