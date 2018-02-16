location = {0: "Quit",
            1: "Road",
            2: "Hill",
            3: "Building",
            4: "Valley",
            5: "Forest"}

exits = {"Q",0}, {"W": 2, "E": 3, "N": 5, "S": 4}, {"N": 5},{"W": 1}, {"W": 2, "N": 1}, {"W": 2, "S": 1}


loc = 1
while True:
    availableExit = " "
    for directions in exits[loc].keys():
    
        availableExit += directions + ","
    print(location[loc])
  
    if loc == 0:
        break
    print("available exits are: " +   availableExit)
    directions = input("please enter a direction: ")
    print()

    if directions in exits[loc]:
        loc = exits[loc][directions]
    else:
        print("you cannot go that direction")
                       
