#!/ysr/env python3
"""This is a short silly script to count the number of gifts in the 12 days of
   of Christmas
"""

from time import sleep

GIFTS = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]


def gift(day):
    """Count gifts Print Text."""
    while day >= 1:
        GIFTS[day-1] += day
        sleep(1)
        day -= 1


for i in range(0, 12):
    gift(i+1)

TOTAL = 0
for i in GIFTS:
    TOTAL += i

# GIFTSSTRING =

print(
    f"Partridges\t{GIFTS[0]}\n"
    f"and Pear Trees:\t{GIFTS[0]}\n"
    f"Turtle Doves:\t\t{GIFTS[1]}\n"
    f"French Hens:\t\t{GIFTS[2]}\n"
    f"Calling Birds:\t\t{GIFTS[3]}\n"
    f"Golden Rings:\t\t{GIFTS[4]}\n"
    f"Geese a-laying:\t{GIFTS[5]}\n"
    f"swans a-swimming:{GIFTS[6]}\n"
    f"French Hens:{GIFTS[7]}\n"
    f"French Hens:{GIFTS[8]}\n"
    f"Total {TOTAL}"
)
