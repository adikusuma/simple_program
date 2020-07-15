num = int(input('masukan bilangan: '))

if num > 1:
    for i in range(2, num):
        if (num % i) == 0:
            print(f'{num} bukan bilangan prima')
            print(f'{i} dikali {num // i} = {num}')
            break
    else:
        print(f'{num} bilangan prima' )

#jika bilangan kurang sari atau sama dengan satu
else:
    print(f'{num} bukan bilangan prima')

