#!/usr/bin/python
import subprocess


def get_quotes(count: int):
    out_text = ""
    for i in range(0, count):
        out_text += subprocess.check_output(["fortune"]).decode("utf-8")
        print(out_text)


def random_encode(in_str: str):

# def read_file():
test_text  = '''
A horse breeder has his young colts bottle-fed after they're three
days old.  He heard that a foal and his mummy are soon parted.

	A horse breeder has his young colts bottle-fed after they're three
days old.  He heard that a foal and his mummy are soon parted.
Making one brilliant decision and a whole bunch of mediocre ones isn't as
good as making a whole bunch of generally smart decisions throughout the
whole process.
		-- John Carmack
'''
