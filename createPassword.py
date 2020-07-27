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

def createPass(passLen):
    
    #According to the answers given, it is an empty list that will contain the elements that may be the password.
    PasswordElements=[]

    if (option1=='Y'):
        continue
        PasswordElements += num
        
    elif (option2=='Y'):
        continue
        PasswordElements += lett
        
    elif (option3=='Y'):
        continue
        PasswordElements += specialchar
        continue
    else:
        print("list is empty therefore password won't create.")
    
    print(PasswordElements)

    #this empty list is gong to contain new password.
    passwordNew=[]

    #create password 
    random.shuffle(passElement)
    passwordNew=passwordNew.append(random.choices(passElement,k=passLen))
    print(passwordNew)
return passwordNew

print("Your new random password: ",createPass())