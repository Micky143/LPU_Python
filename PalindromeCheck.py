#Palindrome Check

word = input("Please Enter The Word:")    
print(word)

reversed_word = word[::-1]

if word == reversed_word:
    print('you are enter the palindrme')
else:
    print('you are did not enter the palindrme')
