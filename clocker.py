import datetime
import time

choice = raw_input("Please type 'in' or 'out' to clock or 'report' to generate an hours report: \n")

with open("clocktimes.txt", "a") as clock_file:
	if choice == "in":
		clock_file.write("Clock In: " + time.strftime("%Y-%m-%d %H:%M") + "\n")
	elif choice == "out":
		clock_file.write("Clock Out: " + time.strftime("%Y-%m-%d %H:%M" + "\n"))