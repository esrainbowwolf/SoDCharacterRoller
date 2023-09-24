#This page is only for testing. Do whatever you want I guess

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


ISSTrait = cv2.imread(r"Traits/IIS_trait.png")
Chemistry = cv2.imread(r"Skills/Chemistry.png")

test2DArray = [[Chemistry,False]]

trait = test2DArray[0][0]
def locateTrait(trait):
    while 1:
        if pyautogui.locateOnScreen(trait, grayscale=True, confidence=0.9) != None:
            print("I can see it")
            ISSloc=pyautogui.locateOnScreen(trait, grayscale=True, confidence=0.9)
            if ISSloc.left>characterOneLeft and ISSloc.left<characterOneRight:
                print("Character One")
            elif ISSloc.left>1070 and ISSloc.left<characterTwoRight:
                print("Character Two")
            elif ISSloc.left>characterThreeLeft and ISSloc.left<characterThreeRight:
                print("Character Three")
            
            time.sleep(0.5)
        else:
            print("I am unable to see it")
            time.sleep(0.5)

locateTrait(trait)