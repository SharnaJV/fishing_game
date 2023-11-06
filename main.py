import time

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
            time.sleep(2)
            return True
        else:
            print("Wrong username or password. Please try again.")
     
if login():
    print("---------------------------------")
    print("          Gone Fishing!          ")
    print("---------------------------------")

    name = input("What is your name?: ")
    answer = input("Would you like to go fishing, " + name + "? \"y\" for yes or \"n\" for no: ")

    if answer == "no" or answer == "n":
        print("Okay, bye for now!")
        exit()
    elif answer == "yes" or answer ==  "y":
        from dice_roller import Die
        die = Die()
        result = die.roll()
        print(result)

# die_roll = 0
# fish_result = list
# create_die = Die(6)
# die_roll = create_die.roll_die()
# fish_array.GetFish(die_roll)
# test = fish_array.get_fish(fish_caught)
# print(fish_array.get_fish(fish_caught))