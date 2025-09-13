def cleaned_string(s):
    return sorted(s.replace(" ","").lower())

word1 = input('Enter the First Word:')
word2 = input('Enter the Second Word:')

if cleaned_string(word1) == cleaned_string(word2):
    print('it is a anagram')
else:
    print('it is not a anagram')