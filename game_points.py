import csv

#this function if for reading from the fish_data file
def r_fish_data():
    fish_data = {}
    with open('fish_data.csv', 'r') as file:
        csv_file = csv.DictReader(file)
        for row in csv_file:
            fish_type = row["Fish type"]
            points_if_kept = int(row["Points if kept"])
            points_if_released = int(row["Points if released"])
            fish_data[fish_type] = (points_if_kept, points_if_released)
    return fish_data

#this function calculates the points based on whether user keeps or releases fish
def points_math(fish_result):
    fish_type = fish_result["fish_type"]
    keep_fish = fish_result["kept"]
    release_fish = fish_result["release"]

    fish_data = r_fish_data()

    if fish_type in fish_data:
        points_if_kept, points_if_released = fish_data[fish_type]
        return points_if_kept if keep_fish == "y" else points_if_released if release_fish == "Y" else 0
    else:
        return 0

