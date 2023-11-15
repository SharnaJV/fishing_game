import time
from user_details import login, getpass
   
#After successful login game intro runs   
def start_game():
    print("---------------------------------")
    print("          Gone Fishing!          ")
    print("---------------------------------")
    time.sleep(1)

    name = input("What is your name?: ")
    answer = input("Would you like to go fishing, " + name + "? \"y\" for yes or \"n\" for no: ")

    if answer == "no" or answer == "n":
        print("Okay, bye for now!")
        exit()
    elif answer == "yes" or answer ==  "y":
#when player says yes to going fishing, the name is sent fishing_results.csv and the dice_roller.py
# functions are initiated
        with open("fishing_results.csv", "a") as file:
            file.write(name +"\n")
        # from dice_roller import Die
        # # die = Die()
        # # result = die.roll()
        from dice_roller import roll_catch
        roll_catch()
username_input = input("Input username then press enter: ")
password_input = getpass("Input password then press enter: ")

if login(username_input, password_input):
    start_game()
else: 
    print("login failed. please try again.")