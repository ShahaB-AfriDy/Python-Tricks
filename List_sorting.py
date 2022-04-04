List = [[2, 7], [7, 3], [3, 8], [8, 7], [9, 7], [4, 9]]
print(List)

print('\nFirst index in inner list base sorted')
first_inner=sorted(List,key=lambda Inner_index:Inner_index[0])
print(first_inner)


Second_inner = sorted(List,key=lambda Inner_index:Inner_index[1])
print('\nSecond index in inner list base sorted')
print(Second_inner)