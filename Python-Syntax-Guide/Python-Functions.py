
# Making a function  ---------------------------------------------------
def function_name():
    print("Hello , this my first Python function!....")


# Passing a single argument -------------------------------------------
def Hello(username):
    print("Hello, "+ username)

Hello('Pythoner:)')


# using positional arguments -------------------------------------------
def flower(flower,color):
    print("\nI have a " + flower + ".")
    print("It is " + color + " color.\n")

flower('rose', 'pink') # call the function with spesific arguments


# Using a default value -------------------------------------------------
def flower2(color,flower='rose'):
    print("\nI have a "+flower+".")
    print("It is "+color+"color.")

flower2('red')


# Using keywords arguments ----------------------------------------------
def flower3(flower,color):
    print("\nI have a "+flower+".")
    print("It is "+color+"color.")

flower3(flower='rose',color='purple')


# Using None to make argument optional -----------------------------------
def flower4(flower,color=None):
    print("\nI have a "+flower+".")
    if color:
        print("It is "+color+".")

flower4('blue')


'''
# Returning a single value ---------------------------------------------
def full_name(first,last):
    return full_name.title()

x=full_name('Trilo','Chan')
print(x)
'''


# Returning a dictionary --------------------------------------------------
def full_name2(first,last):
    person= {'first':first, 'last':last}
    return person

x = full_name2('name','surname')
print(x)


# Passing a list as an argument ------------------------------------------- 
def personal_infos(infos):
    for inf in infos:
        msg = "Hello, " +inf+ " .."
        print(msg)
info_list= ['info1','info2','info3']

personal_infos(info_list)

# ---------------------------------------------------------------