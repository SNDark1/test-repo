x = input('число 1')
y = input('число 2')
max1 = (x > y) * x + (y >= x) * y
print('max' , max1)