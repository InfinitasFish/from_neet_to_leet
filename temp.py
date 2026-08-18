num = 1
# binary shift, 1 is 1, 1 << 2 is 100 in binary, which is 4
print(num << 2)

num = 3
print(num << 1)

list = [1, 2, 3, 4]
# for unequal iterables zip cuts values of larger iterable
for a, b in zip(list, list[1:]):
    print(f"{a} {b}")


# unpacking
list = [1, 2, 3, 4]
num0, *num12 = list
print(num0, num12)
nlist = [5, 6, 7, *list]
print(nlist)

# tuple set
tuple_set = set()
tuple_set.add((1, 1, 2))
tuple_set.add((2, 1, 1))
print(tuple_set)

