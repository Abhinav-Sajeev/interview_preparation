def factorial():
    result = 1
    number = int(input('Enter The number:'))
    for i in range(1,number + 1):
        result *= i 
    print("Factorial is:", result)

factorial()




# output 

# Enter The number:5
# Factorial is: 120