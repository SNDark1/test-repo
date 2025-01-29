x1 = input('число 1')
x2 = input('число 2')
x3 = input('число 3')
f = x1 == x2 == x3
r = x1 == x2 or x2 == x3 or x1 == x3
if f:
    print('3')
elif r:
    print('2')
else:
    print('0')