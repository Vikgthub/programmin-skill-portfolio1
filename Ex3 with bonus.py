# Declare 3 vairables and use user input to store the info
namee = str(input("Please enter your name (first_middle_sur): "))
hometownn = str(input("Enter your hometown: "))
agee = int(input("Enter your age: "))

# Create the dictionary containing the three variables 
dictionary = {
    'name:' : namee ,
    'hometown:' : hometownn ,
    'age:' :agee 
    }

# In dictionary, "a" will print the information in different lines 
for a in dictionary.items():
    print (a)
