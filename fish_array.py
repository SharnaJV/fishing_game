import csv

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

    # if Die.roll == 1:
    #     fdata = list(data_arr[0].values())
    #     fish_caught = fdata[0], fdata[1], fdata[2], fdata[3], fdata[4]
    # elif Die.roll == 2:
    #     fdata = list(data_arr[1].values())
    #     fish_caught = fdata[0], fdata[1], fdata[2], fdata[3], fdata[4]
    # elif Die.roll == 3:
    #     fdata = list(data_arr[2].values())
    #     fish_caught = fdata[0], fdata[1], fdata[2], fdata[3], fdata[4]
    # elif Die.roll == 4:
    #     fdata = list(data_arr[3].values())
    #     fish_caught = fdata[0], fdata[1], fdata[2], fdata[3], fdata[4]
    # elif Die.roll == 5:
    #     fdata = list(data_arr[4].values())
    #     fish_caught = fdata[0], fdata[1], fdata[2], fdata[3], fdata[4]
    # elif Die.roll == 6:
    #     fdata = list(data_arr[5].values())
    #     fish_caught = fdata[0], fdata[1], fdata[2], fdata[3], fdata[4]
    # return fish_caught
