''' program yang menampilkan permutasi dari list '''

from itertools import permutations, combinations, combinations_with_replacement

#
# perm = permutations([1,2,3])
#
# for i in perm:
#     print(i)


# perm = permutations([1,2,3], 2)
#
# for i in perm:
#     print(i)

''' program yang menampilkan combinasi dari list '''

# comb = combinations([1,2,3],2)
#
# for i in comb:
#     print(i)


# comb = combinations([2,1,3], 2)
#
# for i in comb:
#     print(i)


# comb = combinations([1,1,3], 2)
#
# for i in comb:
#     print(i)

comb = combinations_with_replacement([1,2,3], 2)

for i in comb:
    print(i)