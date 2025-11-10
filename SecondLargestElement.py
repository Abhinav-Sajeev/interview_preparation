n = int(input('Enter How many numbers that you want:'))
number = []

for i in range(n):
    a = int(input(f"Enter the {i+1} Element:"))
    number.append(a)

print(f"{number} This is the enterd list")

b = len(number)

for i in range(b-1):
    for j in range(b-i-1):
        if number[j] > number[j+1]:
            number [j], number[j+1] = number[j+1], number[j]

print(f'sorted list',number)

print(f"this is the second largest element:{number[-2]}")



# output 


# Enter How many numbers that you want:5
# Enter the 1 Element:1
# Enter the 2 Element:9
# Enter the 3 Element:4
# Enter the 4 Element:77
# Enter the 5 Element:5
# [1, 9, 4, 77, 5] This is the enterd list
# sorted list [1, 4, 5, 9, 77]
# this is the second largest element:9

