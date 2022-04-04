List = [1,2,3,4,5,6,7,8,9,10]
print(List)

for u in range(len(List)//2):
	Temp = List[u]
	List[u] = List[(len(List)-1)-u]
	List[(len(List)-1)-u] = Temp

print(List)

# note----------------The Rule is simple

# line 4  set the range by half of the lenght of List
# line 5 store first element of the list in Temp variable
# line 6 store last element of list in the first Index of List
# line 7 store first element of list in the last Index of List

# for actual code below
# List = [1,2,3,4,5,6,7,8,9,10]

# print(List)

# for u in range(len(List)//2):
# 	Temp = List[u]
# 	List[u] = List[9-u]
# 	List[9-u] = Temp

# print(List)