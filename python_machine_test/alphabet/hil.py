n = 5

for i in range(n):
    p = 65
    for j in range(i,n):
        print(" ",end=" ")
    for j in range(i):
        print(chr(p),end=" ")
        p+=1
    p-=2
    for j in range(i+1):
        print(chr(p),end=" ")
        p-=1
    print()


# output 
# ------

#           ? 
#         A @ ?
#       A B A @ ?
#     A B C B A @ ?
#   A B C D C B A @ ?