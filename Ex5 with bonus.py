# create a dictionary containg months (as keywords/key) and days in that month (as value)
monthdaysnorm = { "January": 31, "February": 28, "March": 31, "April": 30, "May": 31, "June": 30, "July": 31, "August": 31, "September": 30, "October": 31, "November": 30, "December": 31 }

# create another dictionary with days in a month in a leap year 
monthdaysleapyear = { "January": 31, "February": 29, "March": 31, "April": 30, "May": 31, "June": 30, "July": 31, "August": 31, "September": 30, "October": 31, "November": 30, "December": 31 }

# create variable that stores the month name that user wants 
month = str(input("Enter the MONTH you want to know the days of: "))

# create another variable to capitalize the month (if user inputed without capitalizing first letter) to avoid error
m = month.capitalize()

# create variable that stores the year that user wants 
year = int(input("Enter the year please: "))

# If the year is a leap year then program prints the days in a month in a leap year (eg: 2024,2028)
if year % 4 == 0:
    print ("In a leap year there are: ", monthdaysleapyear[m], "Days in", m,".")
# otherwise it shows the days of a month in a non leap year (eg: 2023,2025)
else:
    print("There are: ", monthdaysnorm[m], "Days in", m,"(in a non-leap year).")
