import csv

global fish_caught
def get_fish(die_roll):
    data_arr =[]
    global fdata
    global fish_caught
    with open("fish_data.csv", 'r') as file:
        csv_file = csv.DictReader(file)
        fish_mapping = {}
        for row in csv_file:
            row = {key.lower(): value for key, value in row.items()}
            fish_item = fish_caught(
                fish_type=row["fish_type"],
                keeper=row["keeper"],
                is_fish=row["is_fish"],
                points_if_kept=row["points_if_kept"],
                points_if_released=row["points_if_released"],
                dice_roll=int(row["dice_roll"])
            )
            data_arr.append(fish_item)
            fish_mapping[int(row["dice_roll"])] = fish_item.fish_type
            
    fish_result = data_arr[die_roll - 1]
    fdata = [fish_result.dice_roll, fish_result.fish_type, fish_result.keeper, fish_result.is_fish, fish_result.points_if_kept, fish_result.points_if_released]
    return fish_item

class fish_caught:
    def __init__(self, dice_roll, fish_type, keeper, is_fish, points_if_kept, points_if_released):
        self.dice_roll = dice_roll
        self.fish_type = fish_type
        self.keeper = keeper
        self.is_fish = is_fish
        self.points_if_kept = points_if_kept
        self.points_if_released = points_if_released
        
    def __str__(self):
        return f"{self.dice_roll}, {self.fish_type}, {self.keeper}, {self.is_fish}, {self.points_if_kept}, {self.points_if_released}"

