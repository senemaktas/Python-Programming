''' The program creates a random password according to the answer by asking the following questions; 
-In the password, it is asked whether there are numbers, letters and special characters.
-The minimum and maximum number of characters should be asked. Special characters -> '! # @ , . $ ''' 

import random

option1=input("Do you want to include numbers? [Y/N]:")
num=random.randint(0,9)

option2=input("Do you want to include letters? [Y/N]:")
letter=["A"]
let=random.choice(letter)

option3=input("Do you want to include special characters? [Y/N]:")
specialcharacter=[" ' " , " ! " , " # " , " @ " , "," , " . " , " $ "]
specialchar=random.choice(specialcharacter)

option4=input("Please enter minimum number of characters:")
option5=input("Please enter maximum number of characters:")
lenPsswd=len(random.randint(min(int(option4)),max(int(option5))))
print