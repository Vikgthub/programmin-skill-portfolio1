# define a function that prints hello when it is called
def hello():
    print ("Hello")
    
# define a function that calls the previous function 
def main():
    hello()

# this part checks if the code is running from another script or same script (main script), if it is it'll run the code 
if __name__ == "__main__":
    main()