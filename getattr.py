# It is the process of looping all the methods of a class instance.

class Sample:
   pass
   
s1=Sample()

for i in dir(s1):
   print(getattr(s1,i))
