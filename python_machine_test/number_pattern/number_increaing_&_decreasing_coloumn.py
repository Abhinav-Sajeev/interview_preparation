n = 5 

for i in range(n):
    p = 1
    for j in range(i,n):
        print(" ",end=" ")
    for j in range(i + 1):
        print(p,end=" ")
        p += 1
    p -= 2
    for q in range(i):
        print(p,end=" ")
        p -= 1
    print()



# output 
# ------

#           1 
#         1 2 1
#       1 2 3 2 1
#     1 2 3 4 3 2 1
#   1 2 3 4 5 4 3 2 1

    