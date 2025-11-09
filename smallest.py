# a = int(input('Enter how many number that u want:'))

# numbers = []

# for i in range(a):
#    numbers.append(int(input(f"Enter the {i+1} number:")))
# print(numbers)


# smallest = numbers[0]
# for num in numbers:
#    if num < smallest:
#       smallest = num

# print("the smallest number is",smallest)


# s = "DoctorPhenomenal"

# for i in range(len(s)):
#    if i % 2 == 0:
#       print(s[i],end="")


# x = 5

# while x >=0:
#    print(x,end=" ")
#    x-=1


# x = 10 
# i = 1

# while i * i <= x:
#    print(i*i,end=" ")
#    i+=1


# x = int(input("Enter the number:"))

# if x == 0:
#    print('already zero')
# elif x < 0:
#    while x <= 0:
#       print(x,end=" ")
#       x+=1
# else:
#    while x >= 0:
#       print(x,end=" ")
#       x-=1



n = int(input("Enter how manay number to u want:"))
number = []
for i in range(n):
    num = int(input(f"Enter the {i+1} number:"))
    number.append(num)

print(number)

smallest = number[0]
for i in number:
    if i < smallest:
        smallest = i

print(f"{smallest} is the smallest in the give input")





# output 

# Enter how manay number to u want:5
# Enter the 1 number:12
# Enter the 2 number:458
# Enter the 3 number:452
# Enter the 4 number:59
# Enter the 5 number:5
# [12, 458, 452, 59, 5]
# 5 is the smallest in the give input