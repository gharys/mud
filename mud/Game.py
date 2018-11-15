import json, os, pathlib

# directory of all save.json files
savedir = "saves"


def save_name(savenum):
    return savedir + "/save" + str(savenum) + ".json"


def save(savenum, data):  # default save procedure
    # variables
    savename = save_name(savenum)
    savelocation = savename
    # variables
    with open(savelocation, "w") as outfile:
        json.dump(data, outfile, indent=3)


def useropenchoice(q):  # asks user to give own input
    print(q)  # q as the question
    var = input()
    while var == "": # checks if input is not empty
        print("You cant enter an empty field!")
        print(q)
        var = input()
    return var


def userchoice(q,*option):  # multiple choice question

    print(q)

    for i in range(len(option)):  # prints all given arguments
        print(i+1, ": ", option[i])
    choice = int(input())

    while  choice < 1 or choice > len(option ):  # checks for valid input
        print("Invalid input!, please choose a number between 1 and ", len(option))
        print(q)
        choice = int(input())
    choice -= 1
    return option[choice]


def newGame():  # starts new game by making a new save file and procedure of making a character

    pathlib.Path(savedir).mkdir(parents=True, exist_ok=True)  # create directory if it not exists

    savenum = 1
    while os.path.isfile(save_name(savenum)):  # check if save file already exitst
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
                }],
            "status_effects": [{

                }]
        }],
        "items": [{
            "key_items": [{

            }],
            "consumables": [{

            }],
            "weapons": [{

            }],
            "armor": [{

            }]
        }]
    }

    # get gender as string via input
    gender = useropenchoice("Give the gender of your hero: ")
    data["character"][0]["gender"] = gender
    save(savenum,data)

    # get name as string via input
    name = useropenchoice("Give a name for your hero: ")
    data["character"][0]["name"] = name
    save(savenum,data)

    # get class via multiple choice
    proffesion = userchoice("What class is your hero", "warrior", "mage", "rogue")
    data["character"][0]["class"] = proffesion
    save(savenum, data)


