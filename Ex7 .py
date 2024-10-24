# create a list containing the names of people
names = [ "Jake", "Zac", "Ian", "Ron", "Sam", "Dave" ]

# create variable that enters a name
search = (input("enter name of the person you want to search for in the name list: "))

# if the name entered by the user is in the created list then program prints message that user is in the list
# the inputed value is also capitalized to avoid errors 
if search.capitalize() in names :
    print ("This Person is available on the list.")
else:
    # otherwise the computer prints the name is not available on the list
    print ("This person not available on the list.")
