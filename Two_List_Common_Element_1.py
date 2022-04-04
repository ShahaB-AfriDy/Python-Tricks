# for other type also work like string,integers,other
# we can use multiple iterables
a = [1, 2, 3, 4]
b = [2, 3, 4, 5]

# use compreshension procedure
# common_x = [x for x in a for y in b if x==y]
# common_y = [y for x in a for y in b if x==y]
# both are same above line 4 and 5
# print(common_y)

# Equivalent the above code

# List = []
# for u in a:
# 	for v in b:
# 		if u==v:
# 			List.append(v)
# print(List)
# --------------------Note--------------------------
# we can use multiple iterables like 3 ,4 etc
# we can use for the problem built-in functions
# a =	set(a)
# b =   set(b)  #list a and b convert into sets
# print(list(a.intersection(b)))
# print(list(set.intersection(set(a),set(b))))