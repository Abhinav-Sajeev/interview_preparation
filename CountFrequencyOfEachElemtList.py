numbers = [2, 3, 2, 5, 3, 2]

frequency = {}

for num in numbers:
    if num in frequency:
        frequency[num] += 1
    else:
        frequency[num] = 1

print(f"This is the frequency count of the list:{frequency}")

 
# output 

# This is the frequency count of the list:{2: 3, 3: 2, 5: 1}