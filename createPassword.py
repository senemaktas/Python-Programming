''' The program creates a random password according to the answer by asking the following questions; 
-In the password, it is asked whether there are numbers, letters and special characters.
-The minimum and maximum number of characters should be asked. Special characters -> '! # @ , . $ ''' 

import random
import string

option1=input("Do you want to include numbers? [Y/N]:")
num=list(string.digits)

option2=input("Do you want to include letters? [Y/N]:")
lett=list(string.ascii_letters)

option3=input("Do you want to include special characters? [Y/N]:")
specialchar=list(string.punctuation)

option4=input("Please enter minimum number of characters:")
option5=input("Please enter maximum number of characters:")

#Random password length is determined from the given values.
passLen=random.randint(int(option4),int(option5))
print("parola uzunluğu: ",passLen)

def createPass():

    #According to the answers given, it is an empty list that will contain the elements that may be the password.
    PasswordElements = list()

    while XXXXXXXXXXXX: 

        if (option1=='N'):
            PasswordElements.extend(num)
            continue
        
        elif (option2=='N'):
            PasswordElements.extend(lett)
            continue
        
        elif (option3=='N'):
            PasswordElements.extend(specialchar)
            continue

        else:
            print("list is empty therefore password won't create.")
    else:
        pass

    print(PasswordElements)

    #this empty list is gong to contain new password.
    passwordNew = list()

    #create password 
    random.shuffle(PasswordElements)
    passwordNew = random.choices(PasswordElements,k=passLen)
    
    return passwordNew

print("Your new random password: ",createPass())