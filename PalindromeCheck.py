#Palindrome Check

word = input("Please Enter The Word:")    
print(word)

reversed_word = word[::-1]

if word == reversed_word:
    print('You are enter the palindrme')
else:
    print('You are did not enter the palindrme')
