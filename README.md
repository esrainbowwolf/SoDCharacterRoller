# SoDCharacterRoller
A character roller for the game State of Decay 2.
The code will automatically check the size of your monitor to decide on positions.
To add more skills/traits you need actual screenshots in the game of said skills (look at already existing images).
You will also need to edit the pathing of these skills in the code because I had issues with mine finding these images without the full path.
You can find how to add more skills to search for in the code section about skills.

There is a "mainTraits" array which searches for your required 3 main traits wanted on each character.
The True/False is meant for the system to continue searching for that trait.
Currently it is set to search for one character with one of each: Unbreakable, Incredible Immune System, and Always Packed a Lunch.
The "secondaryTraits" array is filled with traits/skills you also want the characters to have.
It currently only searches for 2 traits on each character because 3 takes way too long to be worth it.

There is also code that exists that allows you to specify all 3 traits you want your characters have.
This is currently commented out because I see no need in specifying what my characters 100% need.

When initially running the code it will ask if there are any characters you want it to skip.
Use this if there is a character you like already.
