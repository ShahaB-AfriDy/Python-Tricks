# using map function to create nested List from 1 to 10
#  THREE Methods to unpacking the Nested list in python

List = list(map(lambda x:[x],range(1,11)))
print(List)

print('-'*60)
# using List Comprehension to create nested List from 1 to 10
List = [[u] for u in range(1,11)]
print(List)
# using numpy array to create nested list from 1 to 10
# from numpy import array
# List = array(range(1,11)).reshape(-10,1)
# print(List)

print('-'*60)
# now let's unpack the nested list to one list 

# 1 ->>>>>>>>>>>    method number 	ONE

# List = list(map(lambda x:int(*x),List))
# let's Explain the lambda expression x: int(*x) here x = [x]
# i unpacked the list of [x] using * operator then as pass to arg to int class
# print(List)

# ---------------------------------------------------------------------
print('-'*60)
# 2 >>>>>>>>>>>> Method number TWO
# using the comprehension

# List = [int(*u) for u in List]  
# Explain:  int(*u)   here u = [u] so i unpacked the u then as pass arg to int
# print(List)

# ---------------------------------------------------------------------
print('-'*60)
# 3 >>>>>>>>>>>> Method number THREE
# using chain class
from itertools import chain
List = list(chain(*List))
print(List)









