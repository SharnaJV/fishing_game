import random
from fish_array import get_fish

class Die():
    def __init__(self, min_int = 1, max_int = 6):
        self.min_int = min_int
        self.max_int = max_int
    def roll(self):
        return random.randint(self.min_int, self.max_int)
    
die = Die()
roll_again = "yes"

while True:
    roll_again = input("Roll the die? (type \"yes\" or \"y\" then \"Enter\" to roll, anything else with \"Enter\" to quit)")

    if roll_again.lower() == "yes" or roll_again.lower() == "y":
        result = die.roll()
        print("You rolled:", result)
        fish_result = get_fish(result)
        print("Fish Result:")
        for key, value in fish_result.items():
            print(f"{key}: {value}")
    else:
        print("Goodbye!")
        break
    