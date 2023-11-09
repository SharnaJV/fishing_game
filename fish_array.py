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
        "kept" : int(fdata[1]),
        "release" : int(fdata[2])
    }
    return fish_caught

# def fish_dictionary():
#     fish01 = {"Fish Type" : "King George Whiting",
#               "Keep?" : "Y",
#               "Is it a Fish?" : "Y",
#               "Points if Kept" : 50,
#               "Points if Released" : 70}
    
#     fish02 = {"Fish Type" : "Lost Bait",
#               "Keep?" : "N",
#               "Is it a Fish?" : "N",
#               "Points if Kept" : -10,
#               "Points is released" : 0}
    
#     fish03 = {"Fish Type" : "Small Mulloway (undersize)",
#               "Keep?" : "N",
#               "Is it a Fish?" : "Y",
#               "Points if Kept" : -10,
#               "Points is released" : 10}
    
#     fish04 = {"Fish Type" : "Snapper",
#               "Keep?" : "Y",
#               "Is it a Fish?" : "Y",
#               "Points if Kept" : 20,
#               "Points is released" : 20}
    
#     fish05 = {"Fish Type" : "Large Mullet",
#               "Keep?" : "Y",
#               "Is it a Fish?" : "Y",
#               "Points if Kept" : 20,
#               "Points is released" : 20}
    
#     fish06 = {"Fish Type" : "Seaweed Monster (random clump of seaweed)",
#               "Keep?" : "Y",
#               "Is it a Fish?" : "N",
#               "Points if Kept" : 5,
#               "Points is released" : -5}
