#!/ysr/env python3
"""This is a short silly script to count the number of gifts in the 12 days of
   of Christmas
"""

from time import sleep

gifts = [0,0,0,0,0,0,
			0,0,0,0,0,0];

def gift(day):
	while day >= 1:
		gifts[day-1] += day
		day -=1
		
for day in range(0,12):
	gift(day+1)
	# print(day)
total = 0;
for i in gifts:
	total += i

GIFTSSTRING = \
    F"Partridges and Pear Trees:\t{gifts[0]}\n"\
    F"Turtle Doves:\t\t{gifts[1]}\n"\
    F"French Hens:\t\t{gifts[2]}\n"\
    F"Calling Birds:\t\t{gifts[3]}\n"\
    F"Golden Rings:\t\t{gifts[4]}\n"\
    F"Geese a-laying:\t{gifts[5]}\n"\
    F"swans a-swimming:{gifts[6]}\n"\
    F"French Hens:{gifts[7]}\n"\
    F"French Hens:{gifts[8]}\n"\
    F"Total {total}"
    
print(GIFTSSTRING)
