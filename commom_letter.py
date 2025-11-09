def common_letter():
    str1 = input('Enter the first String:')
    str2 = input('Enter the first String:')

    s1 = set(str1)
    s2 = set(str2)

    lst = s1 & s2
    print(lst)

common_letter()





# word1 = input("Enter The First word:")
# word2 = input("Enter The Second word:")

# for i in word1:
#     for j in word2:
#         if i == j:
#             print(f"{i} is the common words ")
#             break





# str1 = input("Enter first string: ")
# str2 = input("Enter second string: ")

# common = []

# for ch in str1:
#     if ch in str2 and ch not in common:
#         common.append(ch)

# print(common)
