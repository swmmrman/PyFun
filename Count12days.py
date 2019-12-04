"""
12 days in python.

This is a short silly script to count the number of gifts,
in the 12 days of Christmas.
"""

from time import sleep
import sys

Z = 0
SLEEP_TIME = 1
GIFTS = [Z] * 12
LINES = [
    "A Partridge in a pear tree",
    "Two Turtle Doves",
    "Three French Hens",
    "4 calling birds",
    "5 gold rings",
    "6 geese a-laying",
    "7 swans a-swimming",
    "8 maids a-milking",
    "9 ladies dancing",
    "10 lords a-leaping",
    "11 pipers piping",
    "12 drummers drumming",
]
UP = "\033[F"


def say_total(first=False):
    """Says the total so far."""
    total = sum(GIFTS) + GIFTS[0]
    wayup = ""
    if not first:
        wayup = UP * 17
    print(
        f"{wayup}"
        f"\033[KPartridges\t\t{GIFTS[0]}\n"
        f"\033[Kand Pear Trees:\t\t{GIFTS[0]}\n"
        f"\033[KTurtle Doves:\t\t{GIFTS[1]}\n"
        f"\033[KFrench Hens:\t\t{GIFTS[2]}\n"
        f"\033[KCalling Birds:\t\t{GIFTS[3]}\n"
        f"\033[KGolden Rings:\t\t{GIFTS[4]}\n"
        f"\033[KGeese a-laying:\t\t{GIFTS[5]}\n"
        f"\033[Kswans a-swimming:\t{GIFTS[6]}\n"
        f"\033[KMaids a-milking:\t{GIFTS[7]}\n"
        f"\033[KLaides Dancing:\t\t{GIFTS[8]}\n"
        f"\033[KLords a-leaping:\t{GIFTS[9]}\n"
        f"\033[KPipers Piping:\t\t{GIFTS[10]}\n"
        f"\033[KDrummers Drumming:\t{GIFTS[11]}\n"
        f"\033[KTotal {total}\n",
        flush=True,
        end=""
    )


def gift(day):
    """Count gifts Print Text."""
    f = day
    while day >= 1:
        GIFTS[day-1] += day
        say_total()
        u = "\033[K"
        print(f"\n{u}Day: {f}\n{u}{LINES[day-1]}\n{u}", flush=True, end="")
        sleep(SLEEP_TIME)
        day -= 1


if(len(sys.argv) > 1):
    arg_one = float(sys.argv[1])
    SLEEP_TIME = arg_one if arg_one > 0 else SLEEP_TIME

say_total(first=True)
print("")
print("")
print("", flush=True)
try:
    for i in range(1, 13):
        gift(i)
except KeyboardInterrupt:
    print("\nBye")

say_total()
print("\n\n")
