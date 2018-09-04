rollno=[1,3,8,2,7]
print(rollno)
seating=[]
rollno.sort()
seating=rollno
print(seating)


#List : finite,ordered,mutable sequence of elements

#extend,insert,remove,clear(),count(),index(value,[start,[stop]]),pop([index])
#sort(key=None,reverse=False)


#Dictionary : Mutable map from hashable values to arbitrary objects

empty={}
print(type(empty))
print(type==dict())


a=dict(one=1,two=2,three=3)
b={"one":1,"two":2,"three":3}
print(a==b)
print(a)
print(b)


myself={"name":"harsha","age":23,"course":"MCA","achievement":"gold medal"}
print(myself)


print(myself['name'])
#print(myself['rollno'])  #it gives KeyError

myself['name']="resham"

print(myself)

myself['college']="LPU"

print(myself)


#Dictionary using list
d={"ABC":[1,2,3],"XYZ":[4,5]}
print(d)

print(d.get("ABC"))
print(d.get("XYZ"))

print(d.get("PQR"))   #used to avoid "not a KeyError"


eng=d.get("English",[])
num_eng=len(eng)
print(num_eng)


del myself['achievement']

print(myself)

print(myself.pop("college"))

print(myself)

print(myself.popitem())
print(myself)


c={"one":1,"two":2,"three":3}
print(c.keys())
print(c.values())
print(c.items())
print(len(c.keys()))

print(('one',1) in c.items())

for value in c.values():
    print(value)

for key in c.keys():
    print(key)

#key_list=list[(c.keys)]
#print(key_list)


x=c.copy()
print(x)



#Tuple : immutalble sequences, collection of heterogenous data like struct in c
#freeze sequences to ensure hashability

t=("harsha","MCA","03-06-1995")
print(t)
print(t[0])


print(len(t))
print(t[1:])  #slicing function
print("harsha" in t)

t1=1234,'ABC',1.2       #packing
print(t1)
print(type(t1))


x,y,z=t1     #unpacking
print(x)
print(y)
print(z)


x1=10
y1=9
print(x1,y1)
x1=x1^y1
y1=x1^y1
x1=x1^y1
print(x1,y1)


x1,y1=y1,x1      #tuple packing
print(x1,y1)


for index,color in enumerate(['red','green','blue']):
    print(index,color)

