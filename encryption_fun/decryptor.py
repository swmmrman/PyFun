#!/usr/bin/python
import random
import sys

encodes = [
    "SIGNS",
    "o'd utzzofu zit iqfu gy ziol enhitk ziofu!",
    "CHATS",
    "viqz vgxsr iqhhtf oy iolzgkn egxsr iqct iorrtf zito k yqetl",
    "ngx'ss wt q hqkz gy zit souiz. ngx vgf'z ltt ziol egdofu. sggk qz igv lzxhor ngx qkt. ngx'ss wt zit gftl zg kthsqet zit uggr dtf vig vtkt zqatf wn ziglt wsxt houl",
    "eiqz",
    "itssg",
    "qfnifc iql lxuqk",
    "eqat",
    "bpg qkt zitn",
    "ntl",
    "io",
    "vt ligxsr aoth ziol jxotz.",
    "ltfr zit dtllqut sqztk...",
    "rgtz ztss qfngft, it douiz wtlztf",
    "lgetgft ol vqzeiofu",
    "zitn e qf'z afgv vt'kt itkt",
    "eqat",
    "igv qkt ngx",
    "ysgvtkl",
    "ittsgggg",
    "o vqfz q ystvtkl",
    "io, viqzsl xh?",
    "vtsegdt!!!",
    "itssg",
    "io vtsegdt!!!",
    "itssg!!",
    "ziqfq ngx",
    "nqnn ! :D",
    "o iqcrt OTHERS",
    "o ltfz ngx dn rgfqzogfl, dq'qd!",
    "oz'l fouiz fgv",
    "vqztk",
    "o vgfrtk viqz zitn'kt",
    "igv qkt nig uxnl",
    "o voss azth stqkfofu tc tkn rqn",
    "HTN lg ziol sqfuxqut ol hktzzn tqln",
    "o qd zknofu z g ktdtdwtk zit stzz tkl",
    "viqz rg ngx ziofa gy oz",
    "ikxxx!",
    "dofofu?",
    "ntl",
    "uggr!!!!! == COOL?",
    "o eqf vsogzt lqd hst ltfztfetl",
    "viqzl xh vozi tuul",
    "sgea of wkg",
    "Mn wqlt ol foet",
    "dn wqlt ol foet",
    "o qd stkfofu ziol sqfuxqut",
    "uktqz",
    "utz dt q rgmtf gy tuul",
    "io, viqzsl xh?",
    "vtsegdt",
    "okgf qbt",
    "egv of wgqz",
    "qbt",
    "vt lgixsr aoth ziol jxotz",
    "sgea of uxnl",
    "qfngft iqct roqdgfrl",
    "qfngft ugz vitqz?",
    "aozzot!!!",
    "wktqr, qfngft??",
    "sgs",
    "yoliotl",
    "egdt gf uxnl",
    "zit aozzn ol ctkn exzt",
    "eqf ngx ztqei dt igv zg wxosr o'd ktqssn wqr qz oz",
    "eqf mass ltt dn qftffq",
]
CYPHER = "kxvmcnophqrszyijadlegwbuft '.,?!:=*"
KEY = "qwertyuiopasdfghjklzxcvbnm  '.,?!:=*"
ALPHA = "abcdefghijklmnopqrstuvwxyz '.,?!:=*"
ALPHA_A_Z = "abcdefghijklmnopqrstuvwxyz"


def encode(clear_text: str):
    outstring: str = ""
    for char in clear_text:
        out_char = ALPHA[CYPHER.find(char.lower())]
        if char.isupper():
            out_char = out_char.upper()
        outstring += out_char
    return outstring


def decode(cypher_text: str):
    outstring: str = ""
    for char in cypher_text:
        out_char = CYPHER[ALPHA.find(char.lower())]
        if char.isupper():
            out_char = out_char.upper()
        outstring += out_char
    return outstring


def decode_all(encodes: list[str]):
    outstring: str = ""
    for encoded in encodes:
        for char in encoded:
            if char.isupper():
                outstring += char
                continue
            outstring += CYPHER[ALPHA.find(char)]
        outstring += "\n"
    return outstring


def decode_loop():
    while True:
        print("String to decode: ", end="")
        print(decode(input()))


def encode_loop():
    while True:
        print("String to encode: ", end="")
        print(encode(input()))


def random_encode(in_file: str, out_file: str):
    clear_text = ""
    with open(in_file, "r") as file:
        clear_text = file.read()
    alpha_list = list(ALPHA_A_Z)
    random.shuffle(alpha_list)
    key = "".join(alpha_list)
    enciphered = ""
    for char in clear_text:
        if char == "\n":
            enciphered += "\n"
            continue
        if char.lower() not in key:
            enciphered += char
            continue
        if char.isupper():
            enciphered += key[ALPHA_A_Z.find(char.lower())].upper()
        else:
            enciphered += key[ALPHA_A_Z.find(char.lower())]
    with open(out_file, "w") as file2:
        file2.write(enciphered)
        file2.close()
        file.close()


if len(sys.argv) >= 2:
    if sys.argv[1] == "decode":
        print(decode(sys.argv[2]))
    elif sys.argv[1] == "encode":
        print(encode(sys.argv[2]))
    elif sys.argv[1] == "idecode":
        decode_loop()
    elif sys.argv[1] == "iencode":
        encode_loop()
    elif sys.argv[1] == "all":
        print(decode_all(encodes))
    elif sys.argv[1] == "fencode":
        random_encode(sys.argv[2], sys.argv[3])
    else:
        print(
            f'Usage: {sys.argv[0]} command "string"\nThe string needs to be in quotes\nCommands:\n\tdecode: decodes\n\tencode: encodes the string\n\tiencode: Interactive encoder\n\t idecode: interactive decoder'
        )

else:
    decode_loop()
