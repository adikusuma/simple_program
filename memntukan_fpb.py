# def hitung_fpb(x, y):
#     ''' fungsi untuk menentukan fpb dari 2 bilangan  '''
#
#     if x > y:
#         smaller = y
#     else:
#         smaller = x
#
#     for i in range(1, smaller+1):
#         if x % i== 0 and y % i == 0:
#             fpb = i
#
#     return fpb
#
# # num1 = 96
# # num2 = 24
#
num1 = int(input('Masukan bilangan pertama: '))
num2 = int(input('Masukan bilangan kedua: '))

#menggunakan algoritma euclidean

def hitung_fpb(x, y):
    ''' fungsi untuk menentukan fpb dari dua bilangan dengan algoritma euclidean '''

    while(y):
        x, y = y, x % y
        return x

# num1 = 200
# num2 = 150
print(f'fpb dari {num1} dan {num2} dengan algoritma euclidean = {hitung_fpb(num1, num2)}')