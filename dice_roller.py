import random
from fish_array import get_fish
import time
from game_points import points_math

class Die():
    def __init__(self, min_int = 1, max_int = 6):
        self.min_int = min_int
        self.max_int = max_int
    def roll(self):
        return random.randint(self.min_int, self.max_int)

def roll_catch():    
    die = Die()
    roll_again = "yes"
    total_points = 0

    while True:
        roll_again = input("Go fishing? (type \"yes\" or \"y\" then \"Enter\" to roll, anything else with \"Enter\" to quit): ")

        if roll_again.lower() == "yes" or roll_again.lower() == "y":
            result = die.roll()
            fish_result = get_fish(result)
            fish_type = fish_result["fish_type"]
            # points_if_kept = points_math(fish_type)
            # points_if_released = points_math(fish_type)
            print("Casting your line...")
            time.sleep(1)
            print("...Waiting for a bite...")
            time.sleep(2)
            print("You have caught a...")
            time.sleep(1)
            print(fish_result["fish_type"])
            keep = input("Would you like to keep your catch? \"y\" or \"n\": ")
            if keep == "y" :
                points_if_kept = points_math(fish_result)
                total_points += points_if_kept
                print(f"For keeping you have earned: {points_if_kept}")
                print(f"Your current score is: {total_points}")
            else:
                points_if_released = points_math(fish_result)
                total_points += points_if_released
                print(f"For releasing you have earned: {points_if_released}")
            print(f"Your current score is: {total_points}")
        else:
            print(f"Your final score is: {total_points} and it has been saved to \"fishing_results.csv\" Goodbye!")
            break

roll_catch()