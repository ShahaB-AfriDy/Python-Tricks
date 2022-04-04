from re import split
# help(split)
# split mehtod return the list of matching pattern

String = input('Enter:>> ')
spliter = split(r'[^0-9.]+',String)
# r[^0-9.]+ all in close braket exclude
# but in this case i.e '21' is included because it is
# different from 21

Filter = list(filter(lambda x:x!='',spliter))
# here we filter the because split method add some
# empty string so that we here remove with help of 
# filter method

print(spliter) # print the match pattern
print(Filter)  # print the filter empty string
print()

Anonymous = lambda x:float(x) if '.' in x else int(x)
#  x contain . or decimal point then i convert into
# float else int
# but Anonymous convert exacty as it is,
Integer_List = list(map(Anonymous,Filter))
# we can use float method direct
# Integer_List = list(map(float,Filter))
print(Integer_List)
