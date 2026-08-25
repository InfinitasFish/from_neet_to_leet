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

# edge range
for i in range(1, 1):
    print(i)  # doesn't print

# edge indexing
list = [1,2,3,4,5]
print(list[1:1])  # empty list

# prefix & suffix
list = [1,2,3,4,5]
pref = [*list]
suf = [*list]
for i in range(1, len(list)):
    pref[i] += pref[i - 1]
for i in range(len(list)-2, -1, -1):
    suf[i] += suf[i+1]
print(f"list: {list}, pref: {pref}, suf: {suf}")

# char ord to detect ints
str = "-109az"
print([ord(c) for c in str])

# module
print(18 % 9)