#what is the operator precedence in python?

print("doesn't")
print("doesn\'t")
print('"Yes" , he said')
print("\"Yes\" , he said")
print('"Isn\'t" ,she said')
print("I\'m in Kolkata but i don\'t know that \"You are also here\". I\'ll see you in Howrah!. But I\'ll request \'You \' to bring \"Rasogulla\" for me.")

#In python everything is object

print(isinstance(4,object))
print(isinstance("Hello",object))
print(isinstance(None,object))
print(isinstance([1,2,3,4],object))

#objects have identity
#id(object) gives objs identity
# "identity" is unique and fixed during an objs lifetime
#objs are tagged with their type at runtime
#objs contain pointers to their data blob.
#this means even small things take up a lot of space

print((4).__sizeof__())

#variable assignment
#in python variables are not copied but they are referenced to each other.
x=123
y=x

#x and y refer to same obj, chnges in x are reflected in y

#duck typing

def compute(a,b,c):
    return(a+b)*c
print(compute(1,2,3))
print(compute([1],[2,3],2))  #[1] is concatenated with [1,2] and output is printed 2 times
print(compute('l','olo',4))

# duck typing here means that for compute() all those manipulations are possible that support + and * operations.

#== is used to check equality and is operator is used to check identity
# eg is checks if both are from same family or not doesnt check inside
# == check if all the specifications are same or not

# use == to check values use is when comparing identities
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


#split ()- converts the string to a list partitioned by a delimiter
print("Hi . How are you ?".split())
print("03-08-1994".split(sep='-'))

#join() creates a string from a given list.
print(' '.join(['harsha','resham','kirti']))


#string formatting
print("{name} loves {food}".format(name='Sam',food='plums'))
print("{0} can be {1} {0}".format('strings','formatted'))
print("{} squared is {}".format(5,5**2))
