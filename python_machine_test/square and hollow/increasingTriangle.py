# n = 5

# for i in range(n):
#     for j in range(n):
#         if (i == n-1 or j == 0 or j == i):
#             print('*',end=" ")
#         else:
#             print(" ",end=" ")
#     print()



# output 
# ------

# *
# * *
# *   *
# *     *
# * * * * *




n = 5

for i in range(n):
    for j in range(i,n):
        if (i == 0 or j == i or j == n -1):
            print('*',end=" ")
        else:
            print(" ",end=" ")
    print()



# output 
# ------

# * * * * * 
# *     *
# *   *
# * *
# *