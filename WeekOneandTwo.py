#This file is for CAP930 Classroom teaching

import this  # The Zen of Python

#Single line Comment is doen using hash
'''
This is how you do multipleline comments

'''

#Variable Declaration

X=2   #No Semicolon is required  # Here X is variable # Python is Dynamic Type #You don't need to define explicitly datatype :) 
print(X)
y=X*7
print(y)


X= "Hello World ! I am "  #String Declartion 
print(X)
print(X+ 'Python')       # Here is String is concatenated


#Variables in Python are dynamically-typed: declared without an explicit type
#objects have a type, so Python knows the type of a variable, even if you don't

print(type(2)) # => <class 'int'>
print(type("Hello")) # => <class 'str'>
print(type(None)) # => <class 'NoneType'>

print(type(int)) # => <class 'type'>
print(type(type(int)))# => <class 'type'>

#Python has two numeric types int and float
print(3) # => 3 (int)
print(3.0) # => 3.0 (float)
print(1 + 1) # => 2
print(8 - 1) # => 7
print(10 * 2 )# => 20
print(9 / 3) # => 3.0
print(5 / 2) # => 2.5
print(7 / 1.4) # => 5.0

print(7 // 3) # => 2 (integer division)
print(7 % 3) # => 1 (integer modulus)
print(2 ** 4 )# => 16 (exponentiation)



#bool is a subtype of int, where True == 1 and False == 0

print(True) # => True
print(False) # => False
print(not True) # => False
print(True and False) # => False
print(True or False )# => True (short-circuits)

print(1== 1 )# => True
print(2 * 3) == 5 # => False
print(1 != 1) # => False
print(2 * 3 != 5) # => True

print(1 < 10) # => True
print(2 >= 0 )# => True
print(1 < 2 < 3) # => True (1 < 2 and 2 < 3)
print(1 < 2 >= 3) # => False (1 < 2 and 2 >= 3)

#No char in Python! Both ' and " create string literals


greeting = 'Hello'
print(greeting)
group = "wørld" # Unicode by default
print(group)

print(greeting + ' ' + group + '!') # => 'Hello wørld!'


#Indexing in Python starts from Zero 0

s='ILOVEPYTHON'
print(s[0] ) # => I
print(s[1])  # => L
print(s[4])  # => E
print(s[6])  # => Y
#print(s[11]) #Error IndexError: string index out of range

#Negative Indexing starts from -1
print(s[-1]) #== N
print(s[-2]) #== O
print(s[-4]) #== T
print(s[-6])#==  P

#Slicing
print(s[0:2]) #== IL
print(s[3:6]) #== VEP
print(s[1:4]) #== LOV

#Slicing Witout START AND STOP
print(s[:2]) #== IL   #Implicitly starts at 0
print(s[3:]) #==VEPYTHON  #Implicitly ends at the end

#Slicing with STEP SIZE
print(s[1:5:2]) #== LV  #Can also pass a step size
print(s[4::-2]) #== EOI #Can also pass a negative step size


#Reversing a String

print(s[::-1]) #==NOHTYPEVOLI




#Converting Values  #Like Storing Mobile Number as string

print(str(55)) # => "42"
print(int("55")) # => 55
print(float("4.5")) # => 4.5


''' List is a Python Data Structure, mutable ,hetrogeneous  and can be nested as well '''

Number =[] #Empty list
print(Number)
Number = [1,2,3]  # List is decalred using squere brackets #Commas separate elements  # Create a new list
print(Number)



'''[] Versatile  Incredibly common  ≈ ArrayList / Vector '''

mixed_list = [10, 9, "Minutes"]  # Lists can contain elements of different types
print(mixed_list)

#Append elements to the end of a list
mixed_list.append(10) # numbers == [10, 9, 'Minutes', 10]
print(mixed_list)
mixed_list.append(115) # numbers == [10, 9, 'Minutes', 10, 115]
print(mixed_list)


# Access elements at a particular index
print(mixed_list[0]) # => 2
print(mixed_list[-1]) # => 11


# You can also slice lists - the same rules apply

print(mixed_list[:3]) # => [10, 9, 'Minutes']
print(mixed_list[1:-1]) # => [9, 'Minutes', 10]

#Nested Lists
Nested_List= [Number,mixed_list]
print(Nested_List)

#Slicing Nested List
print(Nested_List[0])

print(Nested_List[0][1])

print(Nested_List[1][2:])
