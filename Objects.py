print((isinstance(4,object)))

print(isinstance("Hello",object))

print((isinstance([1,2,3],object)))

print(isinstance(None,object))

print((4) .__sizeof__())


def compute(a,b,c): # Duck typing
      return (a+b)*c
a=2
b=4
c=6
print(compute(a,b,c))

print(compute(4,6,7))

print(compute([1],[2,3],2))     # output :- [1, 2, 3, 1, 2, 3]

print(compute('l', 'olo', 4))        # output :-  lolololololololo
