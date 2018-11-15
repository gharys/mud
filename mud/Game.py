import json, os, pathlib

# directory of all save.json files
savedir = "saves"


def save_name(savenum):
    return savedir + "/save" + str(savenum) + ".json"


def save(savenum, data): # default save procedure

    # variables
    savename = save_name(savenum)
    savelocation = savedir + "/" + savename
    # variables
    with open(savelocation, "w") as outfile:
        json.dump(data, outfile, indent=3)


def newGame(): # starts new game by making a new save file

    pathlib.Path(savedir).mkdir(parents=True, exist_ok=True)  # create directory if it not exists

    savenum = 1
    while os.path.isfile(save_name(savenum)): # check if save file already exitst
        savenum += 1

    data = {
        "savenumber": savenum,
        "character": [{
            "gender": "male",
            "name": "0",
            "class": "0",
            "attributes": [{
                "strength": "0",
                "stamina": "0",
                "defence": "0",
                "dexterity": "0",
                "intelligence": "0",
                "charisma": "0",
                "wisdom": "0",
                }]
            }],
        "item": [{
            
        }]
    }

    print("Give the gender for your hero: ")# yes this is a string and not boolean
    gender = input()
    data["character"][0]["gender"] = gender
    save(savenum,data)

    print("Give a name for your hero: ")
    name = input()
    data["character"][0]["name"] = name
    save(savenum,data)

    print("What class is your hero")
    proffesion = input()
    data["character"][0]["class"] = proffesion

