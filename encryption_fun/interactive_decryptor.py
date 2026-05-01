#!/usr/bin/env python
import cypher


def run_command(command, cypher: cypher.cypher):
    parts = command.split(" ")
    print(parts)


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
