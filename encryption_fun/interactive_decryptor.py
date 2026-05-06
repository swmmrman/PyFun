#!/usr/bin/env python
import sys

import cypher


def run_command(input, cypher: cypher.cypher):
    global running
    parts = input.split(" ")
    command = parts[0].lower()
    match command:
        case "print" | "p":
            cypher.print_decrypted()
        case "print_key" | "pk":
            print(c.key)
        case "print_key_sorted" | "pks":
            print(sorted(c.key))
        case "update" | "u":
            if len(parts) < 3:
                print("Missing opperand")
                return
            cypher.update(parts[1], parts[2])
            check = cypher.ceaser_check()
            if check != {}:
                print(f"Possible Ceaser cipher {check}")
        case "mutli" | "m":
            if len(parts) < 3:
                print("Missing opperand")
                return
            cypher.multi_update(parts[1], parts[2])
            check = cypher.ceaser_check()
            if check != {}:
                print(f"Possible Ceaser cipher {check}")
        case "quit" | "q":
            print("goodbye")
            running = False
        case "ceaser_decrypt" | "cd":
            if len(parts) < 2:
                print("Missing shift")
                return
            print(c.ceaser_decrypt(int(parts[1])))
        case "revert" | "r":
            c.revert()
        case "reset":
            c.reset()
            c.print_decrypted()
        case "offsets":
            print(c.decrypted_offsets)
        case "load_text" | "lt":
            c.add_text(" ".join(parts[1:]))
        case "clear_text" | "ct":
            c.clear_text()
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
