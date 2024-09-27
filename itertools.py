from itertools import *
import operator


# product
list_a = [12, 21, 34]
list_b = [13, 31]
prod = product(list_a, list_b)
print(list(prod))


# permutations
print(" permutations   ")
perm = permutations(list_a)
print(list(perm))
perm1 = permutations(list_a, 2)
print(list(perm1))


# combination
print(" combinations   ")
list_a.append(20)
comb = combinations(list_a, 3)
print(list(comb))
comb_rep = combinations_with_replacement(list_a, 2)
print(list(comb_rep))
# accumulate
print(" Accummulate   ")
list_a.insert(3, 92)
print(list_a)
multiplied_accumulated_list = accumulate(list_a, func=max)
print(list(multiplied_accumulated_list))
acc = accumulate(list_a)
print(list(acc))


# groupby_iter
print("Group_by")
vegetables = {'onions', 'kales', 'godjet', 'spinach', 'dania', 'cabbages'}
grouped_by = groupby(vegetables, key=lambda x: x == 'onions')
for key, value in grouped_by:
    print(key, list(value))


print("  count  ")
for nos in count(0):
    if nos == 20:
        break
    print(nos)


print(" repeat ")
cycled_list = [10, 20, 30, 40, ]
for no in repeat(40, 2):
    print(no)




