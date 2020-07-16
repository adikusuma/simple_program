'''calculator sederhana
untuk menjumlah, mengurang, mengkali dan membagi dua bilangan yang diinputkan oleh user
'''

#fungsi menjumlah
def add(x, y):
    return x + y

#fungsi mengurangi
def subtraction(x, y):
    return x - y

#fungsi mengkali
def multiply(x, y):
    return x * y

#fungsi membagi
def divide(x, y):
    return x / y

print('Pilihan Operasi bilangan: ')
print('1. Penjumlahan')
print('2. Pengurangan')
print('3. Perkalian')
print('4. Pembagian')

choise = input('Masukan pilihan operasi (1/2/3/4): ')

num1 =  int(input('Masukan bilangan pertama: '))
num2 = int(input('Masukan bilangan kedua: '))

if choise == '1':
    print(f'{num1} + {num2} adalah {add(num1, num2)}')
elif choise == '2':
    print(f'{num1} - {num2} adalah {subtraction(num1, num2)}')
elif choise == '3':
    print(f'{num1} * {num2} adalah {multiply(num1, num2)}')
elif choise == '4':
    print(f'{num1} / {num2} adalah {divide(num1, num2)}')
else:
    print('Input salah')


if choise == 1:
    print('')



