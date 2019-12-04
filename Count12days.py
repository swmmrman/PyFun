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
	
			
print(
f"Partridges:{gifts[0]}\n"\
f"Turtle Doves:{gifts[1]}\n"\
f"Total {total}")
