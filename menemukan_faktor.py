def print_faktor(x):
    ''' fungsi untuk menampilkan faktor dari bilangan yang diinput '''

    for i in range(1, x+1):
        if x % i == 0:
            print(i)

num = int(input('Masukan bilangan: '))

print_faktor(num)