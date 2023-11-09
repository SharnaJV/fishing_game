import time
import csv

# user login access function
def login():
    while True:
#user will keep being prompted to enter user name and/or password before being allowed to proceed
        user_name = input("Input username then press enter: ")
        while user_name == "":
            user_name = input("You have entered nothing please input username then press enter: ")
        pass_word = input("Input password then press enter: ")
        while pass_word == "":
            pass_word = input("You have entered nothing please input password then press enter: ")

        if user_name == "guest" and pass_word == "guestpass01":
            print("Welcome to ...")
            time.sleep(1)
            return True
        else:
            print("Wrong username or password. Please try again.")
     
if login():
    print("---------------------------------")
    print("          Gone Fishing!          ")
    print("---------------------------------")

    name = input("What is your name?: ")
    answer = input("Would you like to go fishing, " + name + "? \"y\" for yes or \"n\" for no: ")

    if answer == "yes" or answer ==  "y":
        from dice_roller import roll_catch
        with open('fishing_results.csv', 'a') as file:
            writer = csv.writer(file)
            writer.writerow([name])
        roll_catch() 
    
    elif    answer == "no" or answer == "n":
        print("Okay, bye for now!")
        exit()
 
    else:
        print("You are confusing me!")