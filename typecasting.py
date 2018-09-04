a=20
print(type(a))
print(type(str(a)))

#list

abc=[1,2,3,4,5]
print(abc)
empty=[]
print(empty)
mixed=[1,2,'a',"abc"]
print(mixed)
abc.append(6)
abc.append(11)
print(abc)
xyz=abc[:3]  #slicing the list
print(xyz)
print(abc[-1])

#nested list
letters=['a','b','c','d','e']
numbers=[1,2,3,4,5,6]
x=[letters,numbers]
print(x)
