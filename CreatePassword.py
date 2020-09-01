''' The program creates a random password according to the answer by asking the following questions; 
-In the password, it is asked whether there are numbers, letters and special characters.
-The minimum and maximum number of characters should be asked. Special characters -> '! # @ , . $ ''' 

import random
import string

characters = {'lett': list(string.ascii_letters),
              'num': list(string.digits), 
              'punc': list(string.punctuation) }

def createPass(length, opts, chars):
    Password = []
    i = 0
    while i != length:
        Password.append(random.choice(chars[random.choice(opts)]))
        i += 1
    random.shuffle(Password)
    Password = ''.join(Password)
    return Password

option1 = input("Do you want to include letters? [Y/N]: ").lower() == 'y'
option2 = input("Do you want to include numbers? [Y/N]: ").lower() == 'y'
option3 = input("Do you want to include special characters? [Y/N]: ").lower() == 'y'

options = []
if option1:
    options.append('lett')
if option2:
    options.append('num')
if option3:
    options.append('punc')

while True:
    option4 = input("Please enter minimum number of characters: ")
    option5 = input("Please enter maximum number of characters: ")
    try:
        option4 = int(option4)
        option5 = int(option5)
        break
    except ValueError:
        print("Please enter a number.")

passLen = random.randint(option4, option5)

password = createPass(passLen, options, characters)

print(f'Your new password: {password}')
