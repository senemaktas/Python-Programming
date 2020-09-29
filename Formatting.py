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
  
 print("""\n*** {} kere (3,2) geldi *** """.format((j-1)))     
