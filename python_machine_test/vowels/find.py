str1 = 'abhinav'
vowels = 'AEIOUaeiou'
output = ''

for i in str1:
    if i in vowels and i not in output:
        output +=i
print(output)
