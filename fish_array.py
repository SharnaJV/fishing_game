import csv

#this function links the die_roll to the related fish in the fish_data.csv and allows the dice_roller
# to call upon the csv
global fish_caught
def get_fish(die_roll):
    data_arr =[]
    global fdata
    global fish_caught
    with open("fish_data.csv", 'r') as file:
        csv_file = csv.DictReader(file)
        for row in csv_file:
            data_arr.append(dict(row))

    fdata = list(data_arr[die_roll - 1].values())

    fish_caught = {
        "fish_type" : fdata[0],
        "keeper" : fdata[1],
        "is_fish" : fdata[2],
        "kept" : int(fdata[3]),
        "release" : int(fdata[4])
    }
    return fish_caught