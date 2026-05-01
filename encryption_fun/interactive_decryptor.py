#!/usr/bin/env python
import cypher

print("File to read from: [ciphers.txt]")
ans = input()
if ans == "":
    c = cypher.cypher()
else:
    c = cypher.cypher(file=ans)

c.print_decrypted()
