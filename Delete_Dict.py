dd = {"one":1, "two":2, "three":3}
del dd["one"]

print(dd)

#print(dd.pop("three", default))

print(dd.popitem())

print("-------------------------------------------------------------------------------")


ddd = {"one":1, "two":2, "three":3}
print(ddd)
print(ddd.keys())
print(ddd.values())
print(ddd.items())

print(len(ddd.keys()))
#('one', 1) in d.itemes()
#for value in d.values():
#     print(value)
