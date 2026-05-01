#!/usr/bin/env python
import cypher


def run_command(input, cypher: cypher.cypher):
    global running
    parts = input.split(" ")
    command = parts[0]
    match command:
        case "print" | "p":
            cypher.print_decrypted()
        case "update" | "u":
            cypher.update(parts[1], parts[2])
            check = cypher.ceaser_check()
            print(check)
            if check != {}:
                print(f"Possible Ceaser cipher {check}")
        case "quit" | "q":
            print("goodbye")
            running = False
        case _:
            print(f"{command} not recognized. h or help to print help")


print("File to read from: [ciphers.txt]")
ans = input()
if ans == "":
    c = cypher.cypher()
else:
    c = cypher.cypher(file=ans)

c.print_decrypted()

running = True
while running:
    print("Command:")
    command = input()
    run_command(command, c)
