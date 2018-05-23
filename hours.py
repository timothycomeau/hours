from string import *
import re
import math

print("\n+ + + + + + + + + + \n+      Hours      +\n+ + + + + + + + + +\n")

# ==================================================================
# Get input
# ==================================================================

# start=input("\nStart Time: ") #9 am
# end=input("End Time: ")

while True:
	start = input("Start Time: ")
	if "a" in start:
		break
	if "p" in start:
		break

while True:
	end=input("End Time: ")
	if "a" in end:
		break
	if "p" in end:
		break

# ==================================================================
# Parse inputs
# ==================================================================

def timeParser(start_time):
	A= ["10a", "10 am", "10am"]
	B= ["11a", "11 am", "11am"]
	C= ["12a", "12 am", "12am"]

	D= ["10p", "10 pm", "10pm"]
	E= ["11p", "11 pm", "11pm"]
	F= ["12p", "12 pm", "12pm"]

	if '' in start_time:
		start_split = [start_time,'00']
		clock_hours_2 = start_split[0] #returns 9a
		list5 = (re.findall('.', clock_hours_2))
		min_since_midnight = int(list5[0])*60
		minutes = 0

	if '' in start_time and 'p' in start_time:
		# print "PM!"
		start_split = [start_time,'00']
		clock_hours_2 = start_split[0] #returns 9a
		list5 = (re.findall('.', clock_hours_2))
		# print list5
		hours=int(list5[0])+12
		min_since_midnight = hours*60

	# ==================================================================
	# because these times are two digits: 10, 11, 12
	# ==================================================================

	if '' in start_time	and start_time in A:
		# print "10am"
		start_split=['10','00']
		min_since_midnight = 10*60
		minutes = 0
	if '' in start_time	and start_time in B:
		# print "11am"
		start_split=['11','00']
		min_since_midnight = 11*60
		minutes = 0
	if '' in start_time and start_time in C:
		# print "12am"
		start_split=['12','00']
		min_since_midnight = 0
		minutes = 0

	# ==================================================================
	# PM
	# ==================================================================

	if '' in start_time	and start_time in D:
		# print "10pm"
		start_split=['10','00']
		min_since_midnight = 1320
		minutes = 0
	if '' in start_time	and start_time in E:
		# print "11pm"
		start_split=['11','00']
		min_since_midnight = 1380
		minutes = 0
	if '' in start_time and start_time in F:
		# print "12pm"
		start_split=['12','00']
		min_since_midnight = 720
		minutes = 0

	# ==================================================================
	# captures if time is entered as 3:00 or 3.00
	# ==================================================================

	if '.' in start_time:
		start_split = start_time.split('.')
	if ':' in start_time:
		start_split = start_time.split(':')

	clock_hours=start_split[0]
	clock_minutes=start_split[1]
	# print clock_hours, "clock hours"
	# print clock_minutes, "clock minutes"

	list3 = (re.findall('.', clock_minutes))
	# print list3

	list4 = (list3[0],list3[1])
	minutes_rtrv=''.join(list4)
	minutes =int(minutes_rtrv)

	if ('a' in list3 and '12' in clock_hours):
		print("Oy it's midnight")
		min_since_midnight= 0
		minutes = int(minutes)
	elif 'a' in list3:
		# print "AM!"
		min_since_midnight = int(clock_hours)*60

	elif ('p' in list3 and '12' in clock_hours):
		print("Lunch time! Noon!")
		min_since_midnight = 720
	elif 'p' in list3:
		# print "PM!"
		hours=int(clock_hours)+12
		min_since_midnight = hours*60

	# print min_since_midnight, "minutes since midnight"
	# print minutes, "minutes since the hour"
	# print min_since_midnight+minutes, "total minutes since midnight"
	return min_since_midnight+minutes


# ==================================================================
# Run the inputs through the function
# ==================================================================

beginDay=timeParser(start)
endDay=timeParser(end)

# ==================================================================
# Do the math
# ==================================================================

i=float(endDay-beginDay)
j=(i/60)

# ==================================================================
# Outputs
# ==================================================================

print ("overal hours =  {0}".format(j, '.2f'))

# Get lunchtime
lunch=float(input("Lunch? "))

if lunch == 0:
	lunch_min=0
else:
	lunch_min= lunch*60 #30 if 0.5

k = (i-lunch_min)/60

# Print time without lunchtime
# print ("total minus lunch".format(k,'.2f'))
print ("total minus lunch =  {0} hours \n".format(k, '.2f'))

