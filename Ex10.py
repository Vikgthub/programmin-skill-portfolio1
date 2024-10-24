# create variable to get number from user 
numo = int(input("Enter number to check if odd or even: "))

# if variable is divisible by 2 and remainder is 0 then program prints message thay number is even 
if numo % 2 == 0:
    print("The Number You Just Entered Is _Even!")
    # otherwise program prints its odd 
else:
    print("The Number You Just Entered Is _Odd!")
