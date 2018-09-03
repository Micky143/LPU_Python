x = 4
y = 10
print("X",x)
print("Y",y)

temp = x
x = y
y = temp

print(("X",x),("Y",y))


x = x ^ y
y = x ^ y
x = x ^ y

print(("X",x),("Y",y))


x, y = y, x

print(("X",x),("Y",y))
