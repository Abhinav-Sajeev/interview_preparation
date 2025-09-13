num = int(input("Enter the input number:"))
sum = 0
temp = num
n = len(str(num))

while temp > 0:
    digit = temp % 10
    sum += digit ** n
    temp //= 10


if num == sum:
    print("the number is amstrong")
else:
    print('number is not amstrong')


