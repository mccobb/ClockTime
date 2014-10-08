import datetime
import time
import sys

choice = raw_input("Please type 'in' or 'out' to clock or 'report' to generate an hours report: \n")

if choice == "in" or choice == "out":
	with open("clocktimes.txt", "a") as clock_file:
		if choice == "in":
			print("In in")
			clock_file.write("Clock In: " + time.strftime("%Y-%m-%d %H:%M") + "\n")
		elif choice == "out":
			print("In out")
			clock_file.write("Clock Out: " + time.strftime("%Y-%m-%d %H:%M") + "\n")
elif choice == "report":
	# Getting user input
	start_date_str = raw_input("Please enter start date (YYYY-MM-DD): ")
	end_date_str = raw_input("Please enter end date (YYYY-MM-DD): ")

	# Looking at clock times
	clocks = open("clocktimes.txt", "r")

	# Transforming user input into dates
	start_date = time.strptime(start_date_str, "%Y-%m-%d")
	end_date = time.strptime(end_date_str, "%Y-%m-%d")

	# Iterating through clock times to find start 
	current_str = clocks.readline()
	current = time.strptime(current_str[10:20], "%Y-%m-%d")
	print(time.strftime("%Y-%m-%d", current))
	print(time.strftime("%Y-%m-%d", start_date))
	print(time.strftime("%Y-%m-%d", end_date))
	try:
		while(current < start_date):
			print (current < start_date)
			current_str = clocks.readline()
			if(current_str[7:9] == "Out"):
				current_str = clocks.readline()
			current = time.strptime(current_str[10:20], "%Y-%m-%d")
	except:
		# Exiting if invalid start date
		print("Invalid Start Date entered.")
		sys.exit(0)

	# Opening report and putting header
	file report = open("report.txt", "w")
	report.write("Date\tIn\tOut\tHours Worked")

	# Iterating through clocks and arranging them correctly
	while (current - end_date > 0):
		if (current_str[:8] == "Clock In"):
			in_time = time.strptime(current_str[19:], "%H:%M")
			report.write(current.strftime("%m/%d/%y\t%H:%M") + "\t")
			current_str = clocks.readline()
			if (current_str[:9] == "Clock Out"):
				out_time = time.strptime(current_str[20:], "%H:%M")
				report.write(" " + out_time.strftime("%H:%M") + "\t")
				current_str = clocks.readline()
			else:
				report.write(" Did not clock out\n")
		else:


