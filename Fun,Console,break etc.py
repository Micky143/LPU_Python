print(len([]))
print(len("Python"))
print(len([1,2,3,4,5]))

#Membership in()

print('P' in "Python")
print('M' in 'Manish')
print('A' in 'Manish')
print('N' in 'Manish')
print('I' in 'Manish')
print('S' in 'Manish')
print('H' in 'Manishs')

print('apple' in ['banana','mango','orange'])
print('mango' in ['banana','mango','orange'])     

#console IO

#name=input("Enter name : ")
#print("Hello" , name)

#if statements
#no parenthesis,curly brackets
#colon and 4 spaces or a tab
a=4
if a>2:
    print("a greater than 2")
age=17
if age>18:
    print("eligible to vote")
else:
    print("not eligible to vote")
b=0
if b>0:
    print("positive number")
elif b<0:
    print("negative number")
else:
    print("zero")

#palindrome
word=input("enter a word : ")
reversed_word=word[::-1]
if word==reversed_word:
    print("Palindrome")
else:
    print("Non palindrome")

#truthy and falsy

print(bool(None))
print(bool(False))
print(bool(0))
print(bool(0.0))
print(bool(''))

print(bool([]))


data=[]
if data:
    print(data)
else:
    print("Empty")

#loops

#when num of condition is not known its called odd loop.


#for loop
iterable=[1,2,3,4,5]
for item in iterable:
    print(item)

#range used to iterate over a sequence of numbers only
for i in range(3):
    print(i)
print("------------------")
for i in range(5,10):
    print(i)
print("------------------")
for i in range(2,12,3):
    print(i)
print("------------------")
for i in range(-5,-30,-5):
    print(i)
print("------------------")


#break - it takes the control out of the current scope or block

for n in range(10):
    if n==6:
        break;
    print(n, end=',')

#continue

for n in range(10):
    if n%2==0:
        print("Even :" , n)
        continue;
    print("Odd : " , n)

#functions
    #def keyword used to declare and define funcs
    #parameters have no explicit types
    #return is optional, if omitted it returns None

def prime(n):
    for i in range(2,n):
        if n%i==0:
            return False
        return True
n=input("Ënter Number : ")
for x in range(2,int(n)):
    if prime(x):
        print(x, " is prime")

    
