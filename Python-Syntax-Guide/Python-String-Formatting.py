import random

arr=[[],[]]  # create new empty array 

i = 1
j = 1

numbers=[1,2,3,4,5,6]
random.shuffle(numbers)  # mix/shuffle numbers

while i <=100:
  arr[0]=random.choice(numbers)
  arr[1]=random.choice(numbers)
  if arr[0]==3 and arr[1]==2:
     print("""Try {}: \t({},{}) {} *** """.format(i,arr[0],arr[1],j))
     j += 1
  else:
     print("""Try {}: \t({},{}) """.format(i,arr[0],arr[1]))
  i += 1
  
print("""\n*** {} times (3,2) came. *** """.format((j-1)))   


# ----------------------------------------------------------------------------

# ------template----.format() method--positional_arguments------
print(' {0} {1} cost ${2} ' .format(6 , 'bananas' , 1.74))


# ----------------------------------------------------------------------------

# Variables 
name= "Rose"
age= 20

# 1- String formatting using concatenation 
print("My name is " +name+ " , and I am "+str(age)+ " years old.\n")

# 2- String formatting using multiple prints 
print("My name is ", end="")
print(name, end="")
print(", and I am ", end="")
print(age, end="")
print(" years old.\n")

# 3- String formatting using join 
print(''.join(["My name is ", name, " , and I am ", str(age), " years old.\n"]))

# 4- String formatting using modulus operator
print("My name is %s, and I am %d years old.\n" % (name,age))

# 5- String formatting using format function with ordered parameters
print("My name is {}, and I am {} years old.\n".format(name,age))

# 5.1 String formatting using format function with named parameters
print("My name is {n}, and I am {a} years old.\n".format(a=age, n=name))

# 6- String formatting using f-Strings (python 3.6+)
print(f"My name is {name}, and I am {age} years old.\n ")


# ------------------------------------------------------------------------------------