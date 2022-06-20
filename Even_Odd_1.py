# Even and Odd number Simple trick


Even= list(range(0,10,2))
Odd = list(range(1,10,2))
print('Even: ',end=' ')
print(Even)
print('Odd:  ',end=' ')
print(Odd)


# Equivalent code using Compreshension
print('\nCompershension used')
Even = [e for e in range(0,10,2)]
Odd  = [o for o in range(1,10,2) ]

print('Even: ',end=' ')
print(Even)
print('Odd:  ',end=' ')
print(Odd)
#---------------------another Way to the same thing-------------
Even = [e+e for e in range(10//2)]
Odd  = [o+o+1 for o in range(10//2)]

print('Even: ',end=' ')
print(Even)
print('Odd:  ',end=' ')
print(Odd)

import os
os.startfile(os.getcwd())