for i in range(5):
   print(i)

#Break
for n in range(10):
    if n==6:
      break
    print(n, end=',')


#Continue
for n in range(10):
    if n % 2 == 0:
        print('even',n)
        continue
    print('odd',n)
