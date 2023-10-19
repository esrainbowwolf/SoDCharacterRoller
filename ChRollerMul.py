from pyautogui import *
import concurrent.futures
import pyautogui
import numpy as np
import time
import cv2
import os

# Get monitor Size
size = pyautogui.size()
screenWidth = size[0]
screenHeight = size[1]
# Set the charcter bars on right and left side of each character selector for every size monitor
characterOneLeft = screenWidth * 0.18
characterOneRight = screenWidth * 0.35
characterTwoLeft = screenWidth * 0.42
characterTwoRight = screenWidth * 0.58
characterThreeLeft = screenWidth * 0.60
characterThreeRight = screenWidth * 0.80
# The position to move your mouse to for each character
characterOneMousePosition = [
    (characterOneLeft + characterOneRight) / 2,
    screenHeight / 2,
]
characterTwoMousePosition = [
    (characterTwoLeft + characterTwoRight) / 2,
    screenHeight / 2,
]
characterThreeMousePosition = [
    (characterThreeLeft + characterThreeRight) / 2,
    screenHeight / 2,
]


# Checks if there are 3 traits
def checkIfThreeTraits(characterLeft, characterRight, tripleTrait):
    tripleTraitList = list(
        pyautogui.locateAllOnScreen(tripleTrait, grayscale=True, confidence=0.9)
    )
    for i in range(0, len(tripleTraitList)):
        if (
            tripleTraitList[i].left > characterLeft
            and tripleTraitList[i].left < characterRight
        ):
            return True
    return False


# Checks secondary Traits
def loopSecondaryTraits(
    mainTraitLoc, traits, characterLeft, characterRight, tripleTrait
):
    print("Checking secondary stuff\n")

    for trait in traits:
        if pyautogui.locateOnScreen(trait, grayscale=True, confidence=0.9) != None:
            traitLoc = pyautogui.locateOnScreen(trait, grayscale=True, confidence=0.9)
            if (
                traitLoc.left > characterLeft
                and traitLoc.left < characterRight
                and traitLoc != mainTraitLoc
            ):
                if (
                    checkIfThreeTraits(characterLeft, characterRight, tripleTrait)
                    == True
                ):
                    return True

    return False


def searchMainTrait(trait, secondaryTraits, character, tripleTrait):
    if character == "1":
        characterLeft = characterOneLeft
        characterRight = characterOneRight
    elif character == "2":
        characterLeft = characterTwoLeft
        characterRight = characterTwoRight
    elif character == "3":
        characterLeft = characterThreeLeft
        characterRight = characterThreeRight
    else:
        print("Character doesn't exist")
        exit(0)

    if pyautogui.locateOnScreen(trait, grayscale=True, confidence=0.9) != None:
        traitlocOne = pyautogui.locateOnScreen(trait, grayscale=True, confidence=0.9)
        if traitlocOne.left > characterLeft and traitlocOne.left < characterRight:
            found = loopSecondaryTraits(
                traitlocOne, secondaryTraits, characterLeft, characterRight, tripleTrait
            )
            if found == True:
                return True
    return False


def multiProcessCharacters(mainTraits, secondaryTraits, character, tripleTrait):
    traitOne = mainTraits[0][0]
    traitTwo = mainTraits[1][0]
    traitThree = mainTraits[2][0]
    t1Found = mainTraits[0][1]
    t2Found = mainTraits[1][1]
    t3Found = mainTraits[2][1]
    processes = [False, False, False]
    if character == "1":
        pyautogui.moveTo(characterOneMousePosition)
    elif character == "2":
        pyautogui.moveTo(characterTwoMousePosition)
    elif character == "3":
        pyautogui.moveTo(characterThreeMousePosition)
    else:
        print("Character doesn't exist")
        exit(0)

    with concurrent.futures.ThreadPoolExecutor() as executor:
        while t1Found == False or t2Found == False or t3Found == False:
            if t1Found == False:
                f1 = executor.submit(
                    searchMainTrait, traitOne, secondaryTraits, character, tripleTrait
                )
                processes[0] = f1.result()
            if t2Found == False:
                f2 = executor.submit(
                    searchMainTrait, traitTwo, secondaryTraits, character, tripleTrait
                )
                processes[1] = f2.result()
            if t3Found == False:
                f3 = executor.submit(
                    searchMainTrait, traitThree, secondaryTraits, character, tripleTrait
                )
                processes[2] = f3.result()
            if processes[0] == True:
                print("Pair One Done!\n")
                return "1"
            elif processes[1] == True:
                print("Pair Two Done!\n")
                return "2"
            elif processes[2] == True:
                print("Pair Three Done!\n")
                return "3"
            else:
                pyautogui.press(["t"])


# For when you specify every trait you want
def specifyLoopAllCharacters(traitGroups, loopC1, loopC2, loopC3):
    pyautogui.moveTo(characterOneMousePosition)
    while loopC1 == True and (
        traitGroups[0][3] == False
        or traitGroups[1][3] == False
        or traitGroups[2][3] == False
    ):
        if traitGroups[0][3] == False:
            if (
                pyautogui.locateOnScreen(
                    traitGroups[0][0], grayscale=True, confidence=0.9
                )
                != None
                and pyautogui.locateOnScreen(
                    traitGroups[0][1], grayscale=True, confidence=0.9
                )
                != None
                and pyautogui.locateOnScreen(
                    traitGroups[0][2], grayscale=True, confidence=0.9
                )
                != None
            ):
                traitlocOne = pyautogui.locateOnScreen(
                    traitGroups[0][0], grayscale=True, confidence=0.9
                )
                traitlocTwo = pyautogui.locateOnScreen(
                    traitGroups[0][1], grayscale=True, confidence=0.9
                )
                traitlocThree = pyautogui.locateOnScreen(
                    traitGroups[0][2], grayscale=True, confidence=0.9
                )
                if (
                    traitlocOne.left > characterOneLeft
                    and traitlocOne.left < characterOneRight
                    and traitlocTwo.left > characterOneLeft
                    and traitlocTwo.left < characterOneRight
                    and traitlocThree.left > characterOneLeft
                    and traitlocThree.left < characterOneRight
                ):
                    print("Pair One Done!\n")
                    traitGroups[0][3] = True
                    loopC1 = False
        if traitGroups[1][3] == False:
            if (
                pyautogui.locateOnScreen(
                    traitGroups[1][0], grayscale=True, confidence=0.9
                )
                != None
                and pyautogui.locateOnScreen(
                    traitGroups[1][1], grayscale=True, confidence=0.9
                )
                != None
                and pyautogui.locateOnScreen(
                    traitGroups[1][2], grayscale=True, confidence=0.9
                )
                != None
            ):
                traitlocOne = pyautogui.locateOnScreen(
                    traitGroups[1][0], grayscale=True, confidence=0.9
                )
                traitlocTwo = pyautogui.locateOnScreen(
                    traitGroups[1][1], grayscale=True, confidence=0.9
                )
                traitlocThree = pyautogui.locateOnScreen(
                    traitGroups[1][2], grayscale=True, confidence=0.9
                )
                if (
                    traitlocOne.left > characterOneLeft
                    and traitlocOne.left < characterOneRight
                    and traitlocTwo.left > characterOneLeft
                    and traitlocTwo.left < characterOneRight
                    and traitlocThree.left > characterOneLeft
                    and traitlocThree.left < characterOneRight
                ):
                    print("Pair Two Done!\n")
                    traitGroups[1][3] = True
                    loopC1 = False
        if traitGroups[2][3] == False:
            if (
                pyautogui.locateOnScreen(
                    traitGroups[2][0], grayscale=True, confidence=0.9
                )
                != None
                and pyautogui.locateOnScreen(
                    traitGroups[2][1], grayscale=True, confidence=0.9
                )
                != None
                and pyautogui.locateOnScreen(
                    traitGroups[2][2], grayscale=True, confidence=0.9
                )
                != None
            ):
                traitlocOne = pyautogui.locateOnScreen(
                    traitGroups[2][0], grayscale=True, confidence=0.9
                )
                traitlocTwo = pyautogui.locateOnScreen(
                    traitGroups[2][1], grayscale=True, confidence=0.9
                )
                traitlocThree = pyautogui.locateOnScreen(
                    traitGroups[2][2], grayscale=True, confidence=0.9
                )
                if (
                    traitlocOne.left > characterOneLeft
                    and traitlocOne.left < characterOneRight
                    and traitlocTwo.left > characterOneLeft
                    and traitlocTwo.left < characterOneRight
                    and traitlocThree.left > characterOneLeft
                    and traitlocThree.left < characterOneRight
                ):
                    print("Pair Three Done!\n")
                    traitGroups[2][3] = True
                    loopC1 = False
        if loopC1 == True:
            pyautogui.press(["t"])
    print("Character One Done!\n")

    pyautogui.moveTo(characterTwoMousePosition)
    while loopC2 == True and (
        traitGroups[0][3] == False
        or traitGroups[1][3] == False
        or traitGroups[2][3] == False
    ):
        if traitGroups[0][3] == False:
            if (
                pyautogui.locateOnScreen(
                    traitGroups[0][0], grayscale=True, confidence=0.9
                )
                != None
                and pyautogui.locateOnScreen(
                    traitGroups[0][1], grayscale=True, confidence=0.9
                )
                != None
                and pyautogui.locateOnScreen(
                    traitGroups[0][2], grayscale=True, confidence=0.9
                )
                != None
            ):
                traitlocOne = pyautogui.locateOnScreen(
                    traitGroups[0][0], grayscale=True, confidence=0.9
                )
                traitlocTwo = pyautogui.locateOnScreen(
                    traitGroups[0][1], grayscale=True, confidence=0.9
                )
                traitlocThree = pyautogui.locateOnScreen(
                    traitGroups[0][2], grayscale=True, confidence=0.9
                )
                if (
                    traitlocOne.left > characterTwoLeft
                    and traitlocOne.left < characterTwoRight
                    and traitlocTwo.left > characterTwoLeft
                    and traitlocTwo.left < characterTwoRight
                    and traitlocThree.left > characterTwoLeft
                    and traitlocThree.left < characterTwoRight
                ):
                    print("Pair One Done!\n")
                    traitGroups[0][3] = True
                    loopC2 = False
        if traitGroups[1][3] == False:
            if (
                pyautogui.locateOnScreen(
                    traitGroups[1][0], grayscale=True, confidence=0.9
                )
                != None
                and pyautogui.locateOnScreen(
                    traitGroups[1][1], grayscale=True, confidence=0.9
                )
                != None
                and pyautogui.locateOnScreen(
                    traitGroups[1][2], grayscale=True, confidence=0.9
                )
                != None
            ):
                traitlocOne = pyautogui.locateOnScreen(
                    traitGroups[1][0], grayscale=True, confidence=0.9
                )
                traitlocTwo = pyautogui.locateOnScreen(
                    traitGroups[1][1], grayscale=True, confidence=0.9
                )
                traitlocThree = pyautogui.locateOnScreen(
                    traitGroups[1][2], grayscale=True, confidence=0.9
                )
                if (
                    traitlocOne.left > characterTwoLeft
                    and traitlocOne.left < characterTwoRight
                    and traitlocTwo.left > characterTwoLeft
                    and traitlocTwo.left < characterTwoRight
                    and traitlocThree.left > characterTwoLeft
                    and traitlocThree.left < characterTwoRight
                ):
                    print("Pair Two Done!\n")
                    traitGroups[1][3] = True
                    loopC2 = False
        if traitGroups[2][3] == False:
            if (
                pyautogui.locateOnScreen(
                    traitGroups[2][0], grayscale=True, confidence=0.9
                )
                != None
                and pyautogui.locateOnScreen(
                    traitGroups[2][1], grayscale=True, confidence=0.9
                )
                != None
                and pyautogui.locateOnScreen(
                    traitGroups[2][2], grayscale=True, confidence=0.9
                )
                != None
            ):
                traitlocOne = pyautogui.locateOnScreen(
                    traitGroups[2][0], grayscale=True, confidence=0.9
                )
                traitlocTwo = pyautogui.locateOnScreen(
                    traitGroups[2][1], grayscale=True, confidence=0.9
                )
                traitlocThree = pyautogui.locateOnScreen(
                    traitGroups[2][2], grayscale=True, confidence=0.9
                )
                if (
                    traitlocOne.left > characterTwoLeft
                    and traitlocOne.left < characterTwoRight
                    and traitlocTwo.left > characterTwoLeft
                    and traitlocTwo.left < characterTwoRight
                    and traitlocThree.left > characterTwoLeft
                    and traitlocThree.left < characterTwoRight
                ):
                    print("Pair Three Done!\n")
                    traitGroups[2][3] = True
                    loopC2 = False
        if loopC2 == True:
            pyautogui.press(["t"])
    print("Character Two Done!\n")

    pyautogui.moveTo(characterThreeMousePosition)
    while loopC3 == True and (
        traitGroups[0][3] == False
        or traitGroups[1][3] == False
        or traitGroups[2][3] == False
    ):
        if traitGroups[0][3] == False:
            if (
                pyautogui.locateOnScreen(
                    traitGroups[0][0], grayscale=True, confidence=0.9
                )
                != None
                and pyautogui.locateOnScreen(
                    traitGroups[0][1], grayscale=True, confidence=0.9
                )
                != None
                and pyautogui.locateOnScreen(
                    traitGroups[0][2], grayscale=True, confidence=0.9
                )
                != None
            ):
                traitlocOne = pyautogui.locateOnScreen(
                    traitGroups[0][0], grayscale=True, confidence=0.9
                )
                traitlocTwo = pyautogui.locateOnScreen(
                    traitGroups[0][1], grayscale=True, confidence=0.9
                )
                traitlocThree = pyautogui.locateOnScreen(
                    traitGroups[0][2], grayscale=True, confidence=0.9
                )
                if (
                    traitlocOne.left > characterThreeLeft
                    and traitlocOne.left < characterThreeRight
                    and traitlocTwo.left > characterThreeLeft
                    and traitlocTwo.left < characterThreeRight
                    and traitlocThree.left > characterThreeLeft
                    and traitlocThree.left < characterThreeRight
                ):
                    print("Pair One Done!\n")
                    traitGroups[0][3] = True
                    loopC3 = False
        if traitGroups[1][3] == False:
            if (
                pyautogui.locateOnScreen(
                    traitGroups[1][0], grayscale=True, confidence=0.9
                )
                != None
                and pyautogui.locateOnScreen(
                    traitGroups[1][1], grayscale=True, confidence=0.9
                )
                != None
                and pyautogui.locateOnScreen(
                    traitGroups[1][2], grayscale=True, confidence=0.9
                )
                != None
            ):
                traitlocOne = pyautogui.locateOnScreen(
                    traitGroups[1][0], grayscale=True, confidence=0.9
                )
                traitlocTwo = pyautogui.locateOnScreen(
                    traitGroups[1][1], grayscale=True, confidence=0.9
                )
                traitlocThree = pyautogui.locateOnScreen(
                    traitGroups[1][2], grayscale=True, confidence=0.9
                )
                if (
                    traitlocOne.left > characterThreeLeft
                    and traitlocOne.left < characterThreeRight
                    and traitlocTwo.left > characterThreeLeft
                    and traitlocTwo.left < characterThreeRight
                    and traitlocThree.left > characterThreeLeft
                    and traitlocThree.left < characterThreeRight
                ):
                    print("Pair Two Done!\n")
                    traitGroups[1][3] = True
                    loopC3 = False
        if traitGroups[2][3] == False:
            if (
                pyautogui.locateOnScreen(
                    traitGroups[2][0], grayscale=True, confidence=0.9
                )
                != None
                and pyautogui.locateOnScreen(
                    traitGroups[2][1], grayscale=True, confidence=0.9
                )
                != None
                and pyautogui.locateOnScreen(
                    traitGroups[2][2], grayscale=True, confidence=0.9
                )
                != None
            ):
                traitlocOne = pyautogui.locateOnScreen(
                    traitGroups[2][0], grayscale=True, confidence=0.9
                )
                traitlocTwo = pyautogui.locateOnScreen(
                    traitGroups[2][1], grayscale=True, confidence=0.9
                )
                traitlocThree = pyautogui.locateOnScreen(
                    traitGroups[2][2], grayscale=True, confidence=0.9
                )
                if (
                    traitlocOne.left > characterThreeLeft
                    and traitlocOne.left < characterThreeRight
                    and traitlocTwo.left > characterThreeLeft
                    and traitlocTwo.left < characterThreeRight
                    and traitlocThree.left > characterThreeLeft
                    and traitlocThree.left < characterThreeRight
                ):
                    print("Pair Three Done!\n")
                    traitGroups[2][3] = True
                    loopC3 = False
        if loopC3 == True:
            pyautogui.press(["t"])
    print("Character Three Done!\n")


def setNames(mainTraits):
    names = []
    for i in range(len(mainTraits)):
        names.append(str(mainTraits[i][0]))

    finalNames = []
    for i in range(3):
        tempString = names[i]
        slash = tempString.find("/")
        under = tempString.find("_")
        finalNames.append(tempString[slash + 1 : under])

    print(finalNames[:])
    return finalNames


if __name__ == "__main__":
    teamNotMade = True
    user = "y"

    path = os.getcwd()
    # Paths for the folders of skills and traits
    skills_path = path + "\Skills"
    traits_path = path + "\Traits"
    # List of skills and traits
    skills_list = os.listdir(skills_path)
    traits_list = os.listdir(traits_path)
    combined_list = skills_list + traits_list

    # Skills/trait image files implemented
    skillImgList = []
    traitImgList = []

    # Loads images into arrays
    for skill in skills_list:
        tempString = skills_path + "\\" + skill
        image = cv2.imread(tempString)
        skillImgList.append(image)

    for trait in traits_list:
        tempString = traits_path + "\\" + trait
        image = cv2.imread(tempString)
        traitImgList.append(image)

    combinedImgList = skillImgList + traitImgList
    # Used for if three traits exist
    tripleTrait = cv2.imread(r"Three_trait.png")

    # Array used for specifying every trait
    # traitGroups=[[UBTrait,IndefTrait,IndefTrait,False],[ISSTrait,GPhobeTrait,GPhobeTrait,False],[APLTrait,APLTrait,APLTrait,False]]
    # Array used for looking for main trait
    mainTraits = []
    # Array of the main trait names
    mainTraitNames = []
    # Array used for looking for what secondary trait you want
    secondaryTraits = []
    secondaryTraitNames = []
    # timer for tracking how long it takes to get the characters done
    start_time = time.time()

    mainTraitCount = 0
    while mainTraitCount < 3:
        if mainTraitCount == 0:
            print(
                "You can specify one trait/skill for each Character. What 3 traits would you like?"
            )
            for ability in combined_list:
                print(ability)
        usr = input("Choice: ")
        if usr.split(".", 1)[0] in mainTraitNames:
            print("You can't pick that trait again.")
        else:
            if usr in skills_list:
                skillIndex = skills_list.index(usr)
                mainTraits.append([skillImgList[skillIndex], False])
                mainTraitNames.append(skills_list[skillIndex].split(".", 1)[0])
                mainTraitCount += 1
            elif usr in traits_list:
                traitIndex = traits_list.index(usr)
                mainTraits.append([traitImgList[traitIndex], False])
                mainTraitNames.append(traits_list[traitIndex].split(".", 1)[0])
                mainTraitCount += 1
            else:
                print("That does not exist. Try again")

    settingSecondary = True
    goodTraitFound = False
    printTraits = True
    while settingSecondary == True:
        if printTraits == True:
            print(
                "What secondary traits would you like?\nYou must set at least one that is different from all your main traits.\nYou can also type 'all' if you want all of them.\nWhen done type 'done'."
            )
            printTraits = False
            for ability in combined_list:
                print(ability)
        usr = input("Choice: ")
        if usr.split(".", 1)[0] not in mainTraitNames:
            goodTraitFound = True
        if usr == "done":
            if goodTraitFound == False:
                print(
                    "You need to pick at least one trait different from all your main traits."
                )
            else:
                settingSecondary == False
                print("Done setting Secondary ability.")
                break
        elif usr == "all":
            secondaryTraits.clear()
            secondaryTraitNames.clear()
            for x in combinedImgList:
                secondaryTraits.append(x)
            for x in combined_list:
                secondaryTraitNames.append(x.split(".", 1)[0])
            print("Done setting Secondary ability.")
            settingSecondary == False
            goodTraitFound == True
            break
        else:
            if usr in skills_list:
                skillIndex = skills_list.index(usr)
                secondaryTraits.append(skillImgList[skillIndex])
                secondaryTraitNames.append(skills_list[skillIndex].split(".", 1)[0])
            elif usr in traits_list:
                traitIndex = traits_list.index(usr)
                secondaryTraits.append(traitImgList[traitIndex])
                secondaryTraitNames.append(traits_list[traitIndex].split(".", 1)[0])
            else:
                print("That does not exist. Try again")

    # loops all characters at once looking for each trait group
    character = [["1", False], ["2", False], ["3", False]]
    while user != "n":
        traitChosen = False
        characterChosen = False
        print(
            "Did you want to not roll any characters?\nEnter: 1/2/3/n\n1=Character One\n2=Character Two\n3=Character Three\nn=no\n"
        )
        user = input("Choice: ")
        if user == "1":
            character[0][1] = True
            characterChosen = True
        elif user == "2":
            character[1][1] = True
            characterChosen = True
        elif user == "3":
            character[2][1] = True
            characterChosen = True
        elif user == "n":
            print("Character rolling will start in 10 seconds!")
        else:
            print("Not a proper input")
        while characterChosen == True and traitChosen == False:
            print(mainTraitNames[0])
            print(
                "Which trait would you like to reroll?\n"
                + mainTraitNames[0]
                + "\n"
                + mainTraitNames[1]
                + "\n"
                + mainTraitNames[2]
                + "\n"
            )
            traitChoice = input("Choice: ")
            if traitChoice == mainTraitNames[0]:
                mainTraits[0][1] = True
                traitChosen = True
            elif traitChoice == mainTraitNames[1]:
                mainTraits[2][1] = True
                traitChosen = True
            elif traitChoice == mainTraitNames[2]:
                mainTraits[1][1] = True
                traitChosen = True

    # Set main traits, then set your seconday traits/skills you're ok with getting
    while (
        mainTraits[0][1] == False
        or mainTraits[1][1] == False
        or mainTraits[2][1] == False
    ):
        for i in range(10):
            print(str(10 - i))
            sleep(1)
        print("Character rolling starts now!\n")
        print("Rolling for:\n",mainTraitNames[0],"\n",mainTraitNames[1],"\n",mainTraitNames[2])
        if mainTraits[0][1] == False:
            print(mainTraitNames[0])
        if mainTraits[1][1] == False:
            print(mainTraitNames[1])
        if mainTraits[2][1] == False:
            print(mainTraitNames[2])
        for i in range(3):
            if character[i][1] == False:
                print("Starting character ", str(i + 1))
                whichTrait = multiProcessCharacters(
                    mainTraits, secondaryTraits, character[i][0], tripleTrait
                )
                print("Character ", str(i + 1), " Done!\n")
                if whichTrait == "1":
                    mainTraits[0][1] = True
                elif whichTrait == "2":
                    mainTraits[1][1] = True
                elif whichTrait == "3":
                    mainTraits[2][1] = True
                character[i][1] == True

        user = input("Are you happy with these characters? y/n\n")
        if user == "n":
            characterChosen = False
            while characterChosen == False:
                traitChosen = False
                characterChosen = False
                characterChoice = input(
                    "Which character would you like to reroll? 1/2/3\n"
                )
                if characterChoice == "1":
                    character[0][1] = False
                    characterChosen = True
                elif characterChoice == "2":
                    character[1][1] = False
                    characterChosen = True
                elif characterChoice == "3":
                    character[2][1] = False
                    characterChosen = True
                while characterChosen == True and traitChosen == False:
                    print(
                        "Which trait would you like to reroll?",
                        "\n",
                        mainTraitNames[0],
                        "\n",
                        mainTraitNames[1],
                        "\n",
                        mainTraitNames[2],
                        "\n",
                    )
                    traitChoice = input("Choice: ")
                    if traitChoice == mainTraitNames[0]:
                        mainTraits[0][1] = False
                        traitChosen = True
                    elif traitChoice == mainTraitNames[1]:
                        mainTraits[2][1] = False
                        traitChosen = True
                    elif traitChoice == mainTraitNames[2]:
                        mainTraits[1][1] = False
                        traitChosen = True
    # Allows you to specify what 2-3 traits you always want
    """ while traitGroups[0][3]==False or traitGroups[1][3]==False or traitGroups[2][3]==False:
        time.sleep(10)
        print("Character rolling starts now!\n")
        specifyLoopAllCharacters(traitGroups, loopC1, loopC2, loopC3)
        
        if traitGroups[0][3]==False:
            user=input("Trait group one wasn't rolled for. Is this fine? y/n\n")
            if user=='y':
                traitGroups[0][3]=True
        if traitGroups[1][3]==False:
            user=input("Trait group two wasn't rolled for. Is this fine? y/n\n")
            if user=='y':
                traitGroups[1][3]=True
        if traitGroups[2][3]==False:
            user=input("Trait group three wasn't rolled for. Is this fine? y/n\n")
            if user=='y':
                traitGroups[2][3]=True """
    runningMinutes = (time.time() - start_time) / 60
    print("This took: ", str(runningMinutes), " minutes to run")
