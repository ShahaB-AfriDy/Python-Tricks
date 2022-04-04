# def Multiple(a,b,c):
# 	return a*b*c

# print(Multiple(2,3,4))
from math import prod  # function prod

def Multiple(*args):
	return prod(args)

print(Multiple(2,4,3))
# below code is equivalent of that code

# def Multiple(*args):
# 	result = 1
# 	for u in args:
# 		result *= u
# 	return result
# print(Multiple(2,4,3))