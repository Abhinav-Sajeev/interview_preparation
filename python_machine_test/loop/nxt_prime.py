n = int(input("enter a number:"))

def is_prime(num):
    if num % 2 == 1:
        return True
    else:
        return False

num = n +1 
while True:
    if is_prime(num):
        print(f"The first prime greater then {n} is {num}")
        break
    num += 1
