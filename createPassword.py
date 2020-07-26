''' The program creates a random password according to the answer by asking the following questions; 
-In the password, it is asked whether there are numbers, letters and special characters.
-The minimum and maximum number of characters should be asked. Special characters -> '! # @ , . $ ''' 

import random
import string

option1=input("Do you want to include numbers? [Y/N]:")
numberr=list(string.digits)
num=random.choice(numberr)

option2=input("Do you want to include letters? [Y/N]:")
letter=list(string.ascii_letters)
let=random.choice(letter)

option3=input("Do you want to include special characters? [Y/N]:")
specialcharacter=list(string.punctuation)
specialchar=random.choice(specialcharacter)

option4=input("Please enter minimum number of characters:")
option5=input("Please enter maximum number of characters:")
lenPsswd=len(random.randint(min(int(option4)),max(int(option5))))
print("parola uzunluğu: ",lenPsswd)

passwordNew=[]

def createPass():
    if option1==Y:
        passwordNew=passwordNew.append(num)
    elif option2==Y:
        passwordNew=passwordNew.append(let)
    elif option3==Y
       
