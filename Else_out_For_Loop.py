

# “Else” condition inside a “for” loop

# if for loop terminate due to break statement then
# else  will be not execute


List = [2,4,8,12,11]

for u in List:
	if u % 2 == 1:
		print(u)
		break
else:
	print("NO Odd numbers")


