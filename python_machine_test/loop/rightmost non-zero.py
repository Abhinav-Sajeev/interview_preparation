number = [1, 2, 3, 4, 5]
product = 1

for i in number:
    product *=i
print(product)


while product % 10 == 0:
    product //= 10


a = product % 10 

print(a)


# output 

# 120
# 2