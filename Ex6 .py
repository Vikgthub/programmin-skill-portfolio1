# create variable containing the correct password
pas = 12345
# create variable containing nothing in it
inp = ""

# while password is not equal to variable "inp"
while pas != inp:
    # Variable "inp" equals to what user inputs
    inp = int(input("Please enter your password: "))
    # if user input is equal to correct password program prints "access granted"
    if inp == pas:
        print("access granted")
        # if user input is not equal to correct password program prints "try again" to get correct password 
    else: 
      print("please try again!")

