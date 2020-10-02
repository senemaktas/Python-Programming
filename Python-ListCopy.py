num_list=[1,2,3,4,5]

#1 clone a list by brute force 
dublicate_list1=[item for item in num_list]

#2 Clone a list with a slice
dublicate_list2=num_list[:]

#3 Clone a list with the list constructor
dublicate_list3=list(num_list)

#4 Clone a list with the copy function (python 3.3+) , preferred method
dublicate_list4=num_list.copy()

#5 Clone a list with the copy package
import copy
dublicate_list5=copy.copy(num_list)
deep_dublicate_list6=copy.deepcopy(num_list)
