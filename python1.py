import math

def f(a, b, c, x):
    return math.sqrt(x**3 + a * x**2 + b * x + c)

a = int(input('a = '))
b = int(input('b = '))
c = int(input('c = '))
x = int(input('x = '))

print('----------------------')
print('a = ' + str(a))
print('b = ' + str(b))
print('c = ' + str(c))
print('x = ' + str(x))
print('f = ' + str(f(a, b, c, x)))
print('----------------------')

