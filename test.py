import os
import cv2

my_list = [1, 2, 3, 4]

if 4 not in my_list:
    print("5 is not in the list")
else:
    print("5 is in the list")
""" path=os.getcwd()
skills_path=path+"\Skills"
traits_path=path+"\Traits"
skills_list = os.listdir(skills_path)
traits_list = os.listdir(traits_path)

skillImgList=[]
traitImgList=[]

for skill in skills_list:
    tempString=skills_path+"\\"+skill
    image = cv2.imread(tempString)
    skillImgList.append(image)
    
print(skills_list[0])
print(skills_list.index('Chemistry.PNG')) """