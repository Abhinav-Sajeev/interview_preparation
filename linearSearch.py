a = [10, 25, 30, 45, 50, 75, 90]

x = int(input("Enter the number to search:"))

found = False


for i in range(len(a)):
    if a[i] == x:
        print(f"Element found at the index {i}")
        found = True
        break


if not found:
    print('Element not found in the list')


# output 

# Enter the number to search:75
# Element found at the index 5