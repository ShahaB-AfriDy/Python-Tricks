

#First check And because "And" is higher precedence than "or"

print(True or False and False)    # True
print(False or True  and False)   # False


#First check And because "And" is higher precendence than "or"

print(False and True  or False)   # False
print(True and False or False)    # False

#First check And because "And" is higher precendence than "or"

print(True and False and True)    # False
print(True and True and False)    # False