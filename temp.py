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

# string skip indexing
str = "abcd"
for i in range(len(str)):
    print(str[:i] + str[i + 1:])

# lexicographical comparison
print("c" > "bbbbbbbbbbb")  # True
print("bbbbbb" > "b")  # True
print("bba" > "bab")  # True
print("aaaaz" > "bbbbb")  # False
print("ba" > "ab")  # True
print("1234" > "234")  # False
print("1234" > "2")  # False

# negative indexing
list = [1,2,3,4,5]
print(list[:-1])  # [1,2,3,4]

l = [1,2,3]
l0 = [2,1,3]
print(l.__str__() > l0.__str__())  # False

# 2d matrix
m = [[0] * 5] * 5 # btw not correct because each inner list will be pointed at the same memory
m = [[0] * 5 for _ in range(5)]
print(m)

# reverse degree of char
print(ord('a') - 71 - 2 * (ord('a') - 97))
print(ord('b') - 71 - 2 * (ord('b') - 97))
print(ord('c') - 71 - 2 * (ord('c') - 97))
