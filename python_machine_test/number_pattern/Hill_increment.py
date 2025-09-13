# n = 5

# for i in range(n):
#     p = 1
#     for j in range(i,n):
#         print(" ",end=" ")
#     for k in range(i + 1):
#         print(p,end=" ")
#         p += 1
#     for k in range(i):
#         print(p,end=" ")
#         p += 1
#     print()

# output 
# -------

#           1 
#         1 2 3 
#       1 2 3 4 5 
#     1 2 3 4 5 6 7
#   1 2 3 4 5 6 7 8 9



n = 5 
k = 5
for i in range(n):
    p = k
    for j in range(i + 1):
        print(" ",end=" ")
    for q in range(i,n):
        print(p,end=" ")
        p -= 1
    k -= 1
    print()


# output 
# ------

#  5 4 3 2 1 
#     4 3 2 1
#       3 2 1
#         2 1
#           1
