def raise_both(value1,value2):

      new_value1 = value1 ** value2
      new_value2 = value2 ** value1

      new_tuple  = (new_value1,new_value2)
      return new_tuple

print(raise_both(2,3))
