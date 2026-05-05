#!/usr/bin/python
import subprocess


def get_quotes(count: int):
    out_text = ""
    for i in range(0, count):
        out_text += subprocess.check_output(["fortune"]).decode("utf-8")
        print(out_text)


# def read_file():
