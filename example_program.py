# prime or not
# ------------

# num = int(input("ENTER A NUMBER: "))

# if num > 1:
#     for i in range(2,num):
#         if num % i ==0:
#             print(num,"is not a prime number")
#             break
#     else:
#         print(num,"is a prime number")
# else:
#     print(num,"is not a prime number")


# palindrome
# ---------

# s = input("ente a string: ")

# if s == s[::-1]:
#     print("string is a palindrome")
# else:
#     print("string is not palindrome")



# factorial
# ----------

# n = int(input("enter a number: "))
# fact = 1

# for i in range(1,n+1):
#     fact *= i
# print("factorial:",fact)


# fibonacci series 
# ---------------- 

# def fib (n):
#     a,b = 0,1

#     if n==1:
#         print(a)
#     else:
#         print(a)
#         print(b)


#         for i in range(2,n):
#             c = a + b
#             a = b
#             b = c

#             print(c)


# fib(int(input("enter a number: ")))


# string reversal
# --------------

# s = input("ENTER A STRING: ")
# print("reverse format",s[::-1])


# number is even or odd
# ---------------------

# n = int(input("Enter a Number: "))
# if n % 2 ==0:
#     print(n," is even number")
# else:
#     print(n," is odd number")



# sum of n munbers
# ----------------

# n = int(input("ente a number: "))
# total = 0

# for i in range(n):
#     total += i
# print(total)



# largest among three numbres
# --------------------------


# a = int(input("enter the first number: "))
# b = int(input('enter the second number: '))
# c = int(input("enter the third number: "))


# largest = a 

# if b > largest:
#     largest = b
# if c > largest:
#     largest = c 

# print(f"the largest number is {largest}")


# printing patterns
# -----------------


# for i in range(4):
#     for j in range(4):
#         print("* ",end="")

#     print()


# for i in range(4):
#     for j in range(i+1):
#         print("*",end="")
    
#     print()



# for i in range(4):
#     for j in range(4-i):
#         print("*",end="")
    
#     print()


# pyramid
# -------


# n = int(input("ente the number of row: "))

# for i in range(1,n + 1):
#     space = n - i
#     star = 2 * i - 1
#     print(" " * space + "*" * star)


# An Anagram Program
# -------------------

def annagram(str1,str2):
    
    str1 = str1.replace(" ","").lower()
    str2 = str2.replace(" ","").lower()

    return sorted(str1) == sorted(str2)



word1 = input('enter the first word:')
word2 = input('enter the second word:')

if annagram(word1,word2):
    print("the words are annagram")
else:
    print("words are not annagram")
