#import math
from math import sin, cos

a = int (input('Enter a: '))
x = int (input('Enter x: '))

G = 5 * ( -2 * a ** 2 + a * x + 3 * x ** 2)/( -10 * a ** 2 + 11 * a * x + 3 * x ** 2)

F = sin (10 * a ** 2 - 7 * a * x + x ** 2)

Y = sin(1) / cos (45 * a ** 2 - 79 * a * x + 30 * x ** 2)
print('G = {}, F = {}, Y = {}'.format(G, F, Y))