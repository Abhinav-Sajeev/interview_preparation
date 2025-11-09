num = int(input('Enter the number:'))
list1 = []

for n in range(2,num+1):
    for i in range(2,n):
        if n % i == 0:
            break
    else:
        list1.append(n)

print(f"this ate the prime numbers in between {num} : {list1}")

print(f"Sum of the prime numbers {sum(list1)} ")



# output

# Enter the number:10
# this ate the prime numbers in between 10 : [2, 3, 5, 7]
# Sum of the prime numbers 17 