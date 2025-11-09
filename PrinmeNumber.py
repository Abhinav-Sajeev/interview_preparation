num = int(input("enter the number:"))

if num == 1:
    print("the number is not a prime number")

if num > 1:
    for i in range(2,num):
        if num % i == 0:
            print('number is not a prime number')
            break
    else:
        print('number is a prime number')




# output 

# enter the number:11
# number is a prime number