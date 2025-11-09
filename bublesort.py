def bubble_sort(element):
    n = len(element)
    for i in range(n-1):
        for j in range(n-i-1):
            if element[j] > element[j+1]:
                element[j],element[j+1] = element[j+1],element[j]


nums = [5,1,9,4]
bubble_sort(nums)
print(nums)


# output 

# [1, 4, 5, 9]