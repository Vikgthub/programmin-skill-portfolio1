# Create variables for European countries and add their cities as the values
France = "Paris"
Germany = "Berlin"
Italy = "Rome"
Spain = "Madrid"
Norway = "Oslo"
Netherlands = "Amsterdam"
Austria = "Vienna"
Romania = "Bucharest"
Iceland = "Reykjavik"
Slovenia = "Ljubljana"

# In variable one user will input the name of the city
one = str(input("Enter the capital of France: "))
# In variable a1 variable one is capitalized
a1 = one.capitalize()
# If variable a1 is same as variable France then program prints correct answer message, if not then it prints wrong answer message and show the correct answer.
if a1 == France:
    print ("correct answer, greatjob!")
else:
    print ("wrong anwer!!! Correct ans = Paris")
    
# Same applies to other variables and statements
two = str(input("Enter the capital of Germany: "))
b1 = two.capitalize()
if b1 == Germany:
    print ("correct answer, greatjob!")
else:
    print ("wrong anwer!!! Correct ans = Berlin")

three = str(input("Enter the capital of Italy: "))
c1 = three.capitalize()
if c1 == Italy:
    print ("correct answer, greatjob!")
else:
    print ("wrong anwer!!! Correct ans = Rome")

four = str(input("Enter the capital of Spain: "))
d1 = four.capitalize()
if d1 == Spain:
    print ("correct answer, greatjob!")
else:
    print ("wrong anwer!!! Correct ans = Madrid")

five = str(input("Enter the capital of Norway: "))
e1 = five.capitalize()
if e1 == Norway:
    print ("correct answer, greatjob!")
else:
    print ("wrong anwer!!! Correct ans = Oslo" )

six = str(input("Enter the capital of Netherlands: "))
f1 = six.capitalize()
if f1 == Netherlands:
    print ("correct answer, greatjob!")
else:
    print ("wrong anwer!!! Correct ans = Amsterdam")

seven = str(input("Enter the capital of Austria: "))
g1 = seven.capitalize()
if g1 == Austria:
    print ("correct answer, greatjob!")
else:
    print ("wrong anwer!!! Correct ans = Vienna")

eight = str(input("Enter the capital of Romania: "))
h1 = eight.capitalize()
if h1 == Romania:
    print ("correct answer, greatjob!")
else:
    print ("wrong anwer!!! Correct ans = Bucharest")

nine = str(input("Enter the capital of Iceland: "))
i1 = nine.capitalize()
if i1 == Iceland:
    print ("correct answer, greatjob!")
else:
    print ("wrong anwer!!! Correct ans = Reykjavik")
    
ten = str(input("Enter the capital of Slovenia: "))
j1 = ten.capitalize()
if j1 == Slovenia:
    print ("correct answer, greatjob!")
else:
    print ("wrong anwer!!! Correct ans = Ljubljana")
  
 # At the end once the quiz has finished, the programm will print completed quiz message 
print("Congrats, Quiz Completed!")