list1 = [1,4,2,1,5,4,5,9,2,7]
unique = []

for i in list1:
    if i not in unique:
        unique.append(i)
print(unique)