#Single line comment
'''
Multiline comment
'''
x=2
print(x)
y=x+2
print(y)
a='Hello'
print(a+' World')

print(type(2))
print(type("Hello"))
print(type(None))
print(type(4.5))


print(type(int))
print(type(type(int)))

print(3)
print(3.0)
print(7+5)
print(9-8)
print(2*3)
print(8/5)
print(8//5)
print(3**2)
print(10%7)


print(True)
print(False)
print(not True)
print(True and False)
print(True and True)
print(False or True)


print(1==1)
print(4!=5)
print(5!=5)
print((2*3)<=5)
#print(1<10 & 5>4)
print(1<2<3)



s='Hello World'
print(s[0])
#print(s[11])
print(s[-1])
print(s[-2])
print(s[-3])


print(s[0:2])
print(s[3:7])
print(s[:5])
print(s[7:])
print(s[1:7:2])
print(s[::-1])


print(str(55))
print(int(67.9))
print(float(6))


a1=20
print(a1)
print(type(a1))
print(type(str(a1)))


list1=[]
print(list1)
list2=[1,2,3,4,5]
print(list2)
print(len(list2))
list2.append('a')
list2.append(6)
print(list2)
print(list2[-1])

letters=['a','b','c']
numbers=[1,2,3,4]
list3=[letters,numbers]
print(list3)
print(list3[0][0])
print(list3[1][0])


rollno=[4,9,2,7,1,6,10,3]
print(rollno)
seat=[]
rollno.sort()
seat=rollno
print(seat)
seat.insert(0,11)
print(seat)
seat.remove(11)
print(seat)
print(seat.count(6))   #returns the number of times 6 is present in the list
print(min(seat))
print(max(seat))
#print(seat.reverse())
seat.pop(-1)
print(seat)
print(len(seat))




dict1={}
print(dict1)
print(type(dict1))
print(type(dict1)==dict())
d1={"one":1,"two":2,"three":3}
d2=dict(one=1,two=2,three=3)
print(d1==d2)
print(d1)
print(d2)


print(d1['one'])
print(d2['two'])

d1['one']=11
print(d1)


d1['four']=4
print(d1)


d3={"l1":[1,2,3],"l2":["a","b","c"]}
print(d3)
print(d3['l2'])
print(d3.get('l1'))
print(d3.get('l3'))

del d1['four']
print(d1)

#print(d1.pop('one'))
#print(d1)

print(d1.popitem())
print(d1)

print(d2.keys())
print(d2.values())
print(d2.items())

print('one' in d2.keys())


for v in d2.values():
    print(v)

for k in d2.keys():
    print(k)

for k,v in d2.items():
    print(k,v)

x1=d2.copy()
print(x1)

tup=('harsha','3june')
print(tup)
print(tup[1])
print(tup[0:])
print(len(tup))
print('harsha' in tup)
print('r' in tup)



t1=1,2,'a',2.3
print(t1)
print(type(t1))

w,x,y,z=t1
print(w)
print(x)
print(y)
print(z)


for k,v in enumerate(['red','green','blue']):
    print(k,v)



#name=input("Enter name : ")
#print("Hello "+name)


print(bool(None))
print(bool(False))
print(bool(True))
print(bool(0))
print(bool(0.0))
print(bool(''))
print(bool(5))

for i in range(3,15,3):
    print(i, end=' , ')


print(isinstance(4,object))
print(isinstance("Hello",object))
print(isinstance(None,object))
print(isinstance([1,2,3,4],object))


print((5).__sizeof__())


def calc(a,b,c):
    return(a+b)*c

print(calc(1,2,3))
print(calc([1],[2,3],2))
print(calc('l','olo',4))

print(1 is 1.0)
print(1==1.0)
print(type(1)!=type(1.0))




greeting="Hello world !"
print(greeting[4])
print("world" in greeting)
print(len(greeting))
print(greeting.find('lo'))
print(greeting.replace('llo','y'))
print(greeting.startswith('hell'))
print(greeting.isalpha())
print(greeting.lower())
print(greeting.title())
print(greeting.strip())
print(greeting.strip('!'))


print("Hi . How are you ?".split())
print("03-08-1994".split(sep='-'))

print(' '.join(['harsha','resham','kirti']))

print("{name} loves {food}".format(name='Sam',food='plums'))
print("{0} can be {1} {0}".format('strings','formatted'))
print("{} squared is {}".format(5,5**2))





