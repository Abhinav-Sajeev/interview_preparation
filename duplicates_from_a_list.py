def remove_duplicate(number):
    unique = []
    for num in number:
        if num not in unique:
            unique.append(num)
    return unique   


nums = [1, 2, 3, 2, 1, 3, 2, 4, 5, 4]

unique_number = remove_duplicate(nums)
print(unique_number)


# output 

# [1, 2, 3, 4, 5]