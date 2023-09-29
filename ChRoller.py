from pyautogui import *
import pyautogui
import time
import cv2

#Get monitor Size
size=pyautogui.size()
screenWidth=size[0]
screenHeight=size[1]
#Set the charcter bars on right and left side of each character selector for every size monitor
characterOneLeft=screenWidth*.18
characterOneRight=screenWidth*.35
characterTwoLeft=screenWidth*.42
characterTwoRight=screenWidth*.58
characterThreeLeft=screenWidth*.60
characterThreeRight=screenWidth*.80
#The position to move your mouse to for each character
characterOneMousePosition=[(characterOneLeft+characterOneRight)/2, screenHeight/2]
characterTwoMousePosition=[(characterTwoLeft+characterTwoRight)/2, screenHeight/2]
characterThreeMousePosition=[(characterThreeLeft+characterThreeRight)/2, screenHeight/2]

#Screenshots images of character regions
#(starting x, starting y, width, height)
"""
iml=pyautogui.screenshot(region=(478,478,402,97))
iml.save(r"characterOne.png")
iml=pyautogui.screenshot(region=(1075,478,402,97))
iml.save(r"characterTwo.png")
iml=pyautogui.screenshot(region=(1650,478,402,97))
iml.save(r"characterThree.png")
 """
#Checks if there are 3 traits
def checkIfThreeTraits(character):
    tripleTraitList=list(pyautogui.locateAllOnScreen(tripleTrait, grayscale=True, confidence=0.9))
    for i in range(0,len(tripleTraitList)):
        tripleTraitList[i].left
        if character=='1':
            if tripleTraitList[i].left>characterOneLeft and tripleTraitList[i].left<characterOneRight:
                    return True
        elif character=='2':
            if tripleTraitList[i].left>characterTwoLeft and tripleTraitList[i].left<characterTwoRight:
                return True
        elif character=='3':
            if tripleTraitList[i].left>characterThreeLeft and tripleTraitList[i].left<characterThreeRight:
                return True
        else:
            print("Character doesn't exist")
            exit(1)
    
    return False
        
 
def loopSecondaryTraits(mainTraitLoc,character,traits):
    print("Checking secondary stuff\n")
    if character=='1':
        for trait in traits:
            if pyautogui.locateOnScreen(trait, grayscale=True, confidence=0.9) != None:
                traitLoc=pyautogui.locateOnScreen(trait, grayscale=True, confidence=0.9)
                if traitLoc.left>characterOneLeft and traitLoc.left<characterOneRight and traitLoc!=mainTraitLoc:
                    if checkIfThreeTraits(character)==True:
                        return True
            
    elif character=='2':
        for trait in traits:
            if pyautogui.locateOnScreen(trait, grayscale=True, confidence=0.9) != None:
                traitLoc=pyautogui.locateOnScreen(trait, grayscale=True, confidence=0.9)
                if traitLoc.left>characterTwoLeft and traitLoc.left<characterTwoRight and traitLoc!=mainTraitLoc:
                    if checkIfThreeTraits(character)==True:
                        return True
    elif character=='3':
        for trait in traits:
            if pyautogui.locateOnScreen(trait, grayscale=True, confidence=0.9) != None:
                traitLoc=pyautogui.locateOnScreen(trait, grayscale=True, confidence=0.9)
                if traitLoc.left>characterThreeLeft and traitLoc.left<characterThreeRight and traitLoc!=mainTraitLoc:
                    print("Checking if three traits\n")
                    if checkIfThreeTraits(character)==True:
                        return True
    else:
        print("Character doesn't exist")
        exit(1)
    
    return False
    
def specifyLoopAllCharacters(traitGroups, loopC1, loopC2, loopC3):
    pyautogui.moveTo(characterOneMousePosition)
    while loopC1==True and (traitGroups[0][3]==False or traitGroups[1][3]==False or traitGroups[2][3]==False):
        if traitGroups[0][3]==False:
            if pyautogui.locateOnScreen(traitGroups[0][0], grayscale=True, confidence=0.9) != None and pyautogui.locateOnScreen(traitGroups[0][1], grayscale=True, confidence=0.9) != None and pyautogui.locateOnScreen(traitGroups[0][2], grayscale=True, confidence=0.9) != None:
                traitlocOne=pyautogui.locateOnScreen(traitGroups[0][0], grayscale=True, confidence=0.9)
                traitlocTwo=pyautogui.locateOnScreen(traitGroups[0][1], grayscale=True, confidence=0.9)
                traitlocThree=pyautogui.locateOnScreen(traitGroups[0][2], grayscale=True, confidence=0.9)
                if traitlocOne.left>characterOneLeft and traitlocOne.left<characterOneRight and traitlocTwo.left>characterOneLeft and traitlocTwo.left<characterOneRight and traitlocThree.left>characterOneLeft and traitlocThree.left<characterOneRight:
                    print("Pair One Done!\n")
                    traitGroups[0][3]=True
                    loopC1=False
        if traitGroups[1][3]==False:
            if pyautogui.locateOnScreen(traitGroups[1][0], grayscale=True, confidence=0.9) != None and pyautogui.locateOnScreen(traitGroups[1][1], grayscale=True, confidence=0.9) != None and pyautogui.locateOnScreen(traitGroups[1][2], grayscale=True, confidence=0.9) != None:
                traitlocOne=pyautogui.locateOnScreen(traitGroups[1][0], grayscale=True, confidence=0.9)
                traitlocTwo=pyautogui.locateOnScreen(traitGroups[1][1], grayscale=True, confidence=0.9)
                traitlocThree=pyautogui.locateOnScreen(traitGroups[1][2], grayscale=True, confidence=0.9)
                if traitlocOne.left>characterOneLeft and traitlocOne.left<characterOneRight and traitlocTwo.left>characterOneLeft and traitlocTwo.left<characterOneRight and traitlocThree.left>characterOneLeft and traitlocThree.left<characterOneRight:
                    print("Pair Two Done!\n")
                    traitGroups[1][3]=True
                    loopC1=False
        if traitGroups[2][3]==False:
            if pyautogui.locateOnScreen(traitGroups[2][0], grayscale=True, confidence=0.9) != None and pyautogui.locateOnScreen(traitGroups[2][1], grayscale=True, confidence=0.9) != None and pyautogui.locateOnScreen(traitGroups[2][2], grayscale=True, confidence=0.9) != None:
                traitlocOne=pyautogui.locateOnScreen(traitGroups[2][0], grayscale=True, confidence=0.9)
                traitlocTwo=pyautogui.locateOnScreen(traitGroups[2][1], grayscale=True, confidence=0.9)
                traitlocThree=pyautogui.locateOnScreen(traitGroups[2][2], grayscale=True, confidence=0.9)
                if traitlocOne.left>characterOneLeft and traitlocOne.left<characterOneRight and traitlocTwo.left>characterOneLeft and traitlocTwo.left<characterOneRight and traitlocThree.left>characterOneLeft and traitlocThree.left<characterOneRight:
                    print("Pair Three Done!\n")
                    traitGroups[2][3]=True
                    loopC1=False
        if loopC1==True:
            pyautogui.press(['t'])
    print("Character One Done!\n")        
    
    pyautogui.moveTo(characterTwoMousePosition)
    while loopC2==True and (traitGroups[0][3]==False or traitGroups[1][3]==False or traitGroups[2][3]==False):
        if traitGroups[0][3]==False:
            if pyautogui.locateOnScreen(traitGroups[0][0], grayscale=True, confidence=0.9) != None and pyautogui.locateOnScreen(traitGroups[0][1], grayscale=True, confidence=0.9) != None and pyautogui.locateOnScreen(traitGroups[0][2], grayscale=True, confidence=0.9) != None:
                traitlocOne=pyautogui.locateOnScreen(traitGroups[0][0], grayscale=True, confidence=0.9)
                traitlocTwo=pyautogui.locateOnScreen(traitGroups[0][1], grayscale=True, confidence=0.9)
                traitlocThree=pyautogui.locateOnScreen(traitGroups[0][2], grayscale=True, confidence=0.9)
                if traitlocOne.left>characterTwoLeft and traitlocOne.left<characterTwoRight and traitlocTwo.left>characterTwoLeft and traitlocTwo.left<characterTwoRight and traitlocThree.left>characterTwoLeft and traitlocThree.left<characterTwoRight:
                    print("Pair One Done!\n")
                    traitGroups[0][3]=True
                    loopC2=False
        if traitGroups[1][3]==False:
            if pyautogui.locateOnScreen(traitGroups[1][0], grayscale=True, confidence=0.9) != None and pyautogui.locateOnScreen(traitGroups[1][1], grayscale=True, confidence=0.9) != None and pyautogui.locateOnScreen(traitGroups[1][2], grayscale=True, confidence=0.9) != None:
                traitlocOne=pyautogui.locateOnScreen(traitGroups[1][0], grayscale=True, confidence=0.9)
                traitlocTwo=pyautogui.locateOnScreen(traitGroups[1][1], grayscale=True, confidence=0.9)
                traitlocThree=pyautogui.locateOnScreen(traitGroups[1][2], grayscale=True, confidence=0.9)
                if traitlocOne.left>characterTwoLeft and traitlocOne.left<characterTwoRight and traitlocTwo.left>characterTwoLeft and traitlocTwo.left<characterTwoRight and traitlocThree.left>characterTwoLeft and traitlocThree.left<characterTwoRight:
                    print("Pair Two Done!\n")
                    traitGroups[1][3]=True
                    loopC2=False
        if traitGroups[2][3]==False:
            if pyautogui.locateOnScreen(traitGroups[2][0], grayscale=True, confidence=0.9) != None and pyautogui.locateOnScreen(traitGroups[2][1], grayscale=True, confidence=0.9) != None and pyautogui.locateOnScreen(traitGroups[2][2], grayscale=True, confidence=0.9) != None:
                traitlocOne=pyautogui.locateOnScreen(traitGroups[2][0], grayscale=True, confidence=0.9)
                traitlocTwo=pyautogui.locateOnScreen(traitGroups[2][1], grayscale=True, confidence=0.9)
                traitlocThree=pyautogui.locateOnScreen(traitGroups[2][2], grayscale=True, confidence=0.9)
                if traitlocOne.left>characterTwoLeft and traitlocOne.left<characterTwoRight and traitlocTwo.left>characterTwoLeft and traitlocTwo.left<characterTwoRight and traitlocThree.left>characterTwoLeft and traitlocThree.left<characterTwoRight:
                    print("Pair Three Done!\n")
                    traitGroups[2][3]=True
                    loopC2=False
        if loopC2==True:
            pyautogui.press(['t'])
    print("Character Two Done!\n")
    
    pyautogui.moveTo(characterThreeMousePosition)
    while loopC3==True and (traitGroups[0][3]==False or traitGroups[1][3]==False or traitGroups[2][3]==False):
        if traitGroups[0][3]==False:
            if pyautogui.locateOnScreen(traitGroups[0][0], grayscale=True, confidence=0.9) != None and pyautogui.locateOnScreen(traitGroups[0][1], grayscale=True, confidence=0.9) != None and pyautogui.locateOnScreen(traitGroups[0][2], grayscale=True, confidence=0.9) != None:
                traitlocOne=pyautogui.locateOnScreen(traitGroups[0][0], grayscale=True, confidence=0.9)
                traitlocTwo=pyautogui.locateOnScreen(traitGroups[0][1], grayscale=True, confidence=0.9)
                traitlocThree=pyautogui.locateOnScreen(traitGroups[0][2], grayscale=True, confidence=0.9)
                if traitlocOne.left>characterThreeLeft and traitlocOne.left<characterThreeRight and traitlocTwo.left>characterThreeLeft and traitlocTwo.left<characterThreeRight and traitlocThree.left>characterThreeLeft and traitlocThree.left<characterThreeRight:
                    print("Pair One Done!\n")
                    traitGroups[0][3]=True
                    loopC3=False
        if traitGroups[1][3]==False:
            if pyautogui.locateOnScreen(traitGroups[1][0], grayscale=True, confidence=0.9) != None and pyautogui.locateOnScreen(traitGroups[1][1], grayscale=True, confidence=0.9) != None and pyautogui.locateOnScreen(traitGroups[1][2], grayscale=True, confidence=0.9) != None:
                traitlocOne=pyautogui.locateOnScreen(traitGroups[1][0], grayscale=True, confidence=0.9)
                traitlocTwo=pyautogui.locateOnScreen(traitGroups[1][1], grayscale=True, confidence=0.9)
                traitlocThree=pyautogui.locateOnScreen(traitGroups[1][2], grayscale=True, confidence=0.9)
                if traitlocOne.left>characterThreeLeft and traitlocOne.left<characterThreeRight and traitlocTwo.left>characterThreeLeft and traitlocTwo.left<characterThreeRight and traitlocThree.left>characterThreeLeft and traitlocThree.left<characterThreeRight:
                    print("Pair Two Done!\n")
                    traitGroups[1][3]=True
                    loopC3=False
        if traitGroups[2][3]==False:
            if pyautogui.locateOnScreen(traitGroups[2][0], grayscale=True, confidence=0.9) != None and pyautogui.locateOnScreen(traitGroups[2][1], grayscale=True, confidence=0.9) != None and pyautogui.locateOnScreen(traitGroups[2][2], grayscale=True, confidence=0.9) != None:
                traitlocOne=pyautogui.locateOnScreen(traitGroups[2][0], grayscale=True, confidence=0.9)
                traitlocTwo=pyautogui.locateOnScreen(traitGroups[2][1], grayscale=True, confidence=0.9)
                traitlocThree=pyautogui.locateOnScreen(traitGroups[2][2], grayscale=True, confidence=0.9)
                if traitlocOne.left>characterThreeLeft and traitlocOne.left<characterThreeRight and traitlocTwo.left>characterThreeLeft and traitlocTwo.left<characterThreeRight and traitlocThree.left>characterThreeLeft and traitlocThree.left<characterThreeRight:
                    print("Pair Three Done!\n")
                    traitGroups[2][3]=True
                    loopC3=False
        if loopC3==True:
            pyautogui.press(['t'])
    print("Character Three Done!\n")

def optionalLoopAllCharacters(mainTraits,secondaryTraits,loopC1, loopC2, loopC3):
    found=False
    pyautogui.moveTo(characterOneMousePosition)
    while loopC1==True and (mainTraits[0][1]==False or mainTraits[1][1]==False or mainTraits[2][1]==False):
        if mainTraits[0][1]==False:
            if pyautogui.locateOnScreen(mainTraits[0][0], grayscale=True, confidence=0.9) != None:
                traitlocOne=pyautogui.locateOnScreen(mainTraits[0][0], grayscale=True, confidence=0.9)
                if traitlocOne.left>characterOneLeft and traitlocOne.left<characterOneRight:
                    found=loopSecondaryTraits(traitlocOne,'1',secondaryTraits)
                    if found==True:
                        print("Pair One Done!\n")
                        mainTraits[0][1]=True
                        loopC1=False
                        found=False
        if mainTraits[1][1]==False:
            if pyautogui.locateOnScreen(mainTraits[1][0], grayscale=True, confidence=0.9) != None:
                traitlocOne=pyautogui.locateOnScreen(mainTraits[1][0], grayscale=True, confidence=0.9)
                if traitlocOne.left>characterOneLeft and traitlocOne.left<characterOneRight:
                    found=loopSecondaryTraits(traitlocOne,'1',secondaryTraits)
                    if found==True:
                        print("Pair Two Done!\n")
                        mainTraits[1][1]=True
                        loopC1=False
                        found=False
        if mainTraits[2][1]==False:
            if pyautogui.locateOnScreen(mainTraits[2][0], grayscale=True, confidence=0.9) != None:
                traitlocOne=pyautogui.locateOnScreen(mainTraits[2][0], grayscale=True, confidence=0.9)
                if traitlocOne.left>characterOneLeft and traitlocOne.left<characterOneRight:
                    found=loopSecondaryTraits(traitlocOne,'1',secondaryTraits)
                    if found==True:
                        print("Pair Three Done!\n")
                        mainTraits[2][1]=True
                        loopC1=False
                        found=False
        if loopC1==True:
            pyautogui.press(['t'])
    print("Character One Done!\n")        
    
    pyautogui.moveTo(characterTwoMousePosition)
    while loopC2==True and (mainTraits[0][1]==False or mainTraits[1][1]==False or mainTraits[2][1]==False):
        if mainTraits[0][1]==False:
            if pyautogui.locateOnScreen(mainTraits[0][0], grayscale=True, confidence=0.9) != None:
                traitlocOne=pyautogui.locateOnScreen(mainTraits[0][0], grayscale=True, confidence=0.9)
                if traitlocOne.left>characterTwoLeft and traitlocOne.left<characterTwoRight:
                    found=loopSecondaryTraits(traitlocOne,'2',secondaryTraits)
                    if found==True:
                        print("Pair One Done!\n")
                        mainTraits[0][1]=True
                        loopC2=False
                        found=False
        if mainTraits[1][1]==False:
            if pyautogui.locateOnScreen(mainTraits[1][0], grayscale=True, confidence=0.9) != None:
                traitlocOne=pyautogui.locateOnScreen(mainTraits[1][0], grayscale=True, confidence=0.9)
                if traitlocOne.left>characterTwoLeft and traitlocOne.left<characterTwoRight:
                    found=loopSecondaryTraits(traitlocOne,'2',secondaryTraits)
                    if found==True:
                        print("Pair Two Done!\n")
                        mainTraits[1][1]=True
                        loopC2=False
                        found=False
        if mainTraits[2][1]==False:
            if pyautogui.locateOnScreen(mainTraits[2][0], grayscale=True, confidence=0.9) != None:
                traitlocOne=pyautogui.locateOnScreen(mainTraits[2][0], grayscale=True, confidence=0.9)
                if traitlocOne.left>characterTwoLeft and traitlocOne.left<characterTwoRight:
                    found=loopSecondaryTraits(traitlocOne,'2',secondaryTraits)
                    if found==True:
                        print("Pair Three Done!\n")
                        mainTraits[2][1]=True
                        loopC2=False
                        found=False
        if loopC2==True:
            pyautogui.press(['t'])
    print("Character Two Done!\n")
    
    pyautogui.moveTo(characterThreeMousePosition)
    while loopC3==True and (mainTraits[0][1]==False or mainTraits[1][1]==False or mainTraits[2][1]==False):
        if mainTraits[0][1]==False:
            if pyautogui.locateOnScreen(mainTraits[0][0], grayscale=True, confidence=0.9) != None:
                traitlocOne=pyautogui.locateOnScreen(mainTraits[0][0], grayscale=True, confidence=0.9)
                if traitlocOne.left>characterThreeLeft and traitlocOne.left<characterThreeRight:
                    found=loopSecondaryTraits(traitlocOne,'3',secondaryTraits)
                    if found==True:
                        print("Pair One Done!\n")
                        mainTraits[0][1]=True
                        loopC3=False
                        found=False
        if mainTraits[1][1]==False:
            if pyautogui.locateOnScreen(mainTraits[1][0], grayscale=True, confidence=0.9) != None:
                traitlocOne=pyautogui.locateOnScreen(mainTraits[1][0], grayscale=True, confidence=0.9)
                if traitlocOne.left>characterThreeLeft and traitlocOne.left<characterThreeRight:
                    found=loopSecondaryTraits(traitlocOne,'3',secondaryTraits)
                    if found==True:
                        print("Pair Two Done!\n")
                        mainTraits[0][1]=True
                        loopC3=False
                        found=False
        if mainTraits[2][1]==False:
            if pyautogui.locateOnScreen(mainTraits[2][0], grayscale=True, confidence=0.9) != None:
                traitlocOne=pyautogui.locateOnScreen(mainTraits[2][0], grayscale=True, confidence=0.9)
                if traitlocOne.left>characterThreeLeft and traitlocOne.left<characterThreeRight:
                    found=loopSecondaryTraits(traitlocOne,'3',secondaryTraits)
                    if found==True:
                        print("Pair Three Done!\n")
                        mainTraits[0][1]=True
                        loopC3=False
                        found=False
        if loopC3==True:
            pyautogui.press(['t'])
    print("Character Three Done!\n")

teamNotMade=True
loopC1=True
loopC2=True
loopC3=True
user=''

#Traits implemented
tripleTrait = cv2.imread(r"Three_trait.png")
ISSTrait = cv2.imread(r"Traits/IIS_trait.png")
UBTrait = cv2.imread(r"Traits/UB_trait.png")
APLTrait = cv2.imread(r"Traits/APL_trait.png")
GPhobeTrait = cv2.imread(r"Traits/GPhobe_trait.png")
IndefTrait = cv2.imread(r"Traits/Indef_trait.png")
CareTrait = cv2.imread(r"Traits/Care_trait.PNG")
HLCTrait = cv2.imread(r"Traits/HLC_trait.PNG")
ImmTrait = cv2.imread(r"Traits/Imm_trait.PNG")
EncourTrait = cv2.imread(r"Traits/Encour_trait.PNG")
FDTrait = cv2.imread(r"Traits/FD_trait.PNG")
HoHTrait = cv2.imread(r"Traits/HoH_trait.PNG")
HPTTrait = cv2.imread(r"Traits/HPT_trait.PNG")
FSTrait = cv2.imread(r"Traits/FS_trait.PNG")
HSFTrait = cv2.imread(r"Traits/HSF_trait.PNG")
PETrait = cv2.imread(r"Traits/PE_trait.PNG")
LACTrait = cv2.imread(r"Traits/LAC_trait.PNG")
ELaBTrait = cv2.imread(r"Traits/ELaB_trait.PNG")
KETrait = cv2.imread(r"Traits/KE_trait.PNG")
NBSTrait = cv2.imread(r"Traits/NBS_trait.PNG")
SBiPTrait = cv2.imread(r"Traits/SBiP_trait.PNG")
HTTrait = cv2.imread(r"Traits/HT_trait.PNG")
PANTrait = cv2.imread(r"Traits/PAN_trait.PNG")
GHTrait = cv2.imread(r"Traits/GH_trait.PNG")
SotGTrait = cv2.imread(r"Traits/SotG_trait.PNG")

#Skills implemented
Hygiene = cv2.imread(r"Skills/Hygiene.PNG")
Chemistry = cv2.imread(r"Skills/Chemistry.PNG")
Cooking = cv2.imread(r"Skills/Cooking.PNG")

traitGroups=[[UBTrait,IndefTrait,IndefTrait,False],[ISSTrait,GPhobeTrait,GPhobeTrait,False],[APLTrait,APLTrait,APLTrait,False]]
mainTraits=[[UBTrait,False],[ISSTrait,False],[Cooking,False]]
secondaryTraits=[SotGTrait,GHTrait,PANTrait,HTTrait,SBiPTrait,NBSTrait,KETrait,ELaBTrait,LACTrait, PETrait, HSFTrait,Chemistry,FSTrait,HPTTrait,HoHTrait,FDTrait,EncourTrait,ImmTrait,IndefTrait,HLCTrait,UBTrait,ISSTrait,Hygiene]
#timer for tracking how long it takes to get the characters done
start_time=time.time()

#Used for testing if we can even find that trait
""" while 1:
    if pyautogui.locateOnScreen(Hygiene, grayscale=True, confidence=0.9) != None:
        print("I can see it")
        ISSloc=pyautogui.locateOnScreen(Hygiene, grayscale=True, confidence=0.9)
        if ISSloc.left>characterOneLeft and ISSloc.left<characterOneRight:
            print("Character One")
        elif ISSloc.left>1070 and ISSloc.left<characterTwoRight:
            print("Character Two")
        elif ISSloc.left>characterThreeLeft and ISSloc.left<characterThreeRight:
            print("Character Three")
        
        time.sleep(0.5)
        break
    else:
        print("I am unable to see it")
        time.sleep(0.5) """

#loops all characters at once looking for each trait group
while user!='n':
    user=input("Did you want to not roll any characters?\nEnter: 1/2/3/n\n1=Character One\n2=Character Two\n3=Character Three\nn=no\n")
    if user=='1':
        loopC1=False
    elif user=='2':
        loopC2=False
    elif user=='3':
        loopC3=False
    elif user=='n':
        print("Character rolling will start in 10 seconds!\n")

#Set main traits, then set your seconday traits/skills you're ok with getting
while mainTraits[0][1]==False or mainTraits[1][1]==False or mainTraits[2][1]==False:
    for i in range(10):
        print(str(10-i))
        sleep(1)
    print("Character rolling starts now!\n")
    optionalLoopAllCharacters(mainTraits,secondaryTraits,loopC1, loopC2, loopC3)
    
    if mainTraits[0][1]==False:
        user=input("Trait group one wasn't rolled for. Is this fine? y/n\n")
        if user=='y':
            traitGroups[0][1]=True
    if mainTraits[1][1]==False:
        user=input("Trait group two wasn't rolled for. Is this fine? y/n\n")
        if user=='y':
            traitGroups[1][1]=True
    if mainTraits[2][1]==False:
        user=input("Trait group three wasn't rolled for. Is this fine? y/n\n")
        if user=='y':
            traitGroups[2][1]=True
       
#Allows you to specify what 2-3 traits you always want
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
    
print ("This took:"+str((time.time()-start_time)/60)+ "minutes to run")