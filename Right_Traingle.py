def Right_Triangle(Number=5):
    for i in range(1,Number+1):
        previous_number = 0
        for j in range(1,i+1):
            print((previous_number+i), end=' ')
            previous_number += Number-j
        print()

Right_Triangle()
# 1st example if Number = 5
#               Different with previous number           
# 1             -- or 0
# 2 6           4 
# 3 7 10        4 3      
# 4 8 11 13     4 3 2
# 5 9 12 14 15  4 3 2 1

# 2nd example if Number = 6
#                   Different with previous number           
# 1                 -- or 0
# 2 7               5
# 3 8 12            5 4
# 4 9 13 16         5 4 3 
# 5 10 14 17 19     5 4 3 2
# 6 11 15 18 20 21  5 4 3 2 1
