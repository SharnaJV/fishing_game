import random
from fish_array import get_fish
import time

#this is the die class
class Die():
    def __init__(self, min_int = 1, max_int = 6):
        self.min_int = min_int
        self.max_int = max_int
    def roll(self):
        return random.randint(self.min_int, self.max_int)

#this function will ask the user to roll the die. if user responds with a "n" the game ends
#if user responds with "y" the dies is rolled and users will recieve the related result from the 
#fish data.csv

def roll_catch():    
    die = Die()
    total_points = 0

    while True:
        roll_again = input("Roll the die? (type \"yes\" or \"y\" then \"Enter\" to roll, anything else with \"Enter\" to quit): ")

        if roll_again.lower() == "yes" or roll_again.lower() == "y":
            result = die.roll()
            fish_result = get_fish(result)

            print("Casting your line...")
            time.sleep(1)
            print("...Waiting for a bite...")
            time.sleep(2)
            print("You have caught a...")
            time.sleep(1)
            print(fish_result["fish_type"])
            time.sleep(1)
            print("Keeping the " + fish_result["fish_type"] + ", will award you: " + str(fish_result["kept"]) + " points.")
            print("Releasing the " + fish_result["fish_type"] + ", will award you: " + str(fish_result["release"]) + " points.")
            #Here is where the points for each catch are calculated the printed in terminal
            keep = input("Would you like to keep your catch? \"y\" or \"n\": ")
            if keep == "y" :
                kpoints_math = fish_result["kept"]
                total_points += kpoints_math
                print(f"For keeping you have earned: {kpoints_math}")
                print(f"Your current score is: {total_points}")
            elif keep == "n":
                rpoints_math = fish_result["release"]
                total_points += rpoints_math
                print(f"For releasing you have earned: {rpoints_math}")
                print(f"Your current score is: {total_points}")
        else:
            #when player has finished, total score is saved to fishing_results.csv and game ends
            with open("fishing_results.csv", "a") as file:
                file.write("total Score: " + str(total_points) + "\n\n")
            print(f"Your final score is: {total_points} and it has been saved to \"fishing_results.csv\" Goodbye!")
            break
