#menyelesaikan persaam kuadrad dari ax2 + bx + c = 0

import math

a = int(input('Masukan a: '))
b = int(input('Masukan b: '))
c = int(input('Masukan c: '))


#menghitung diskriminan d
d = (b**2) - (4*a*c)

#menghitung x1 dan x2

x1 = (-b + math.sqrt(d)) / (2*a)
x2 = (-b - math.sqrt(d)) / (2*a)

print((f'solusinya adalah {x1} dan {x2}'))

