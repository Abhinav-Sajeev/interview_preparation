n = 5 
p = 1

for i in range(n-1):
    for j in range(i,n):
        print(" ",end=" ")
    for k in range(i + 1):
        print(p,end=" ")
    for q in range(i):
        print(p,end=" ")
    p += 1
    print()

for i in range(n):
    for j in range(i + 1):
        print(" ",end=" ")
    for k in range(i,n):
        print(p,end=" ")
    for q in range(i,n-1):
        print(p,end=" ")
    p += 1
    print()


# output 
# ------

#           1 
#         2 2 2 
#       3 3 3 3 3 
#     4 4 4 4 4 4 4 
#   5 5 5 5 5 5 5 5 5 
#     6 6 6 6 6 6 6 
#       7 7 7 7 7 
#         8 8 8 
#           9