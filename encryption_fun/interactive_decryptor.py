#!/usr/bin/env python

import sys

encoded_text = ""
with open(sys.argv[1], "r") as cypher_file:
    encoded_text = cypher_file.read()

print(encoded_text)
