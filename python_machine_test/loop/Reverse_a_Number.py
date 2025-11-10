n = int(input("Enter the number that want to reverse:"))
rev = 0

while n > 0:
    digit = n % 10
    rev = rev * 10 + digit
    n //= 10

print(rev)

# output 

# Enter the number to be reverse:1245
# 5421
