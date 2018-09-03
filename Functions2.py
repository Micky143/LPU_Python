
greeting ="hello World.!"
print(greeting)  
 
print(greeting.find('lo'))     #output :- 3

print(greeting.replace('llo', 'y'))   #output :- hey World.!

print(greeting.startswith('hell'))  #output :- True

print(greeting.isalpha())   #output :-  False


greeting = "Micky Mehra..!"

print(greeting.lower())
print(greeting.title())  #output :-  Micky Mehra..!

print(greeting.strip())    #output :-  Micky Mehra..!
print(greeting.strip('!'))   #output :-  Micky Mehra..  (no Show  ' ! ' )

g="ram and shayam".split()   #output :- ['ram', 'and', 'shayam']
print(g)

date='2-12-2000'.split(sep='-')   #output :-   ['2', '12', '2000']
print(date)

fnd_name = ','.join(['Micky','Shujma'])
print(fnd_name)
