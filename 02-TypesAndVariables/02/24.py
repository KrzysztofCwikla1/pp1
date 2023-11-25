import math
a=(int(input('input a')))
b=(int(input('input b')))
c=(int(input('input c')))
p=0.5*(a+b+c)
area1=(p*(p-a)*(p-b)*(p-c))
pierwiastek= math.sqrt(area1)
print(pierwiastek)
print(f'obwód równa się {a+b+c}')