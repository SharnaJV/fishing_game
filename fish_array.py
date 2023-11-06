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

def fish_dictionary():
    fish01 = {"Fish Type" : "King George Whiting",
              "Keep?" : "Y",
              "Is it a Fish?" : "Y",
              "Points if Kept" : 50,
              "Points if Released" : 70}
    
    fish02 = {"Fish Type" : "Lost Bait",
              "Keep?" : "N",
              "Is it a Fish?" : "N",
              "Points if Kept" : -10,
              "Points is released" : 0}
    
    fish03 = {"Fish Type" : "Small Mulloway (undersize)",
              "Keep?" : "N",
              "Is it a Fish?" : "Y",
              "Points if Kept" : -10,
              "Points is released" : 10}
    
    fish04 = {"Fish Type" : "Snapper",
              "Keep?" : "Y",
              "Is it a Fish?" : "Y",
              "Points if Kept" : 20,
              "Points is released" : 20}
    
    fish05 = {"Fish Type" : "Large Mullet",
              "Keep?" : "Y",
              "Is it a Fish?" : "Y",
              "Points if Kept" : 20,
              "Points is released" : 20}
    
    fish06 = {"Fish Type" : "Seaweed Monster (random clump of seaweed)",
              "Keep?" : "Y",
              "Is it a Fish?" : "N",
              "Points if Kept" : 5,
              "Points is released" : -5}

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
