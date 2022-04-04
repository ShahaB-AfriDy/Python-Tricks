# from itertools import chain

# in this case sum() and ''.join() function will not work
# and also chain class no worked here

# multiple type data like list tuple,list-digit
List = [(3),[6,2],[4,8],0,(1,[5]),[9,(7)]]
print(List)

# create compreshension list
# first convert List into string then check if list has not
# these elements "[(,)] " and at the end white space
# then assign to list or append to list
					
					# use    if  u.isdigit() instead of
List = [u for u in str(List) if u not in "[(,)] "]
print(List)

# use map function  convert each element into int type then assign to List object
List = list(map(int,sorted(List)))
print(List) # use sorted(List,reverse=True) for reverse
# instead using map for string we can do with ''.join function

# print(''.join(sorted(List))) #join can convert into integer

# _______________Very Short code the above problem______________
# no need the  map functon  in one line of code will solve
# List = sorted([int(u) for u in str(List) if u.isdigit()])
# print(List)



