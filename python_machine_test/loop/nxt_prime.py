n = int(input("Enter the number:"))

def is_prime(num):
    if num > 1:
        for i in range(2,num):
            if num % i == 0:
                return False
        else:
            return True
        
number = n + 1
while True:
    if is_prime(number):
        print("the next prime number is",number)
        break
    number += 1