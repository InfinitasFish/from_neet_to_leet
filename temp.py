num = 1
# binary shift, 1 is 1, 1 << 2 is 100 in binary, which is 4
print(num << 2)

num = 3
print(num << 1)

list = [1, 2, 3, 4]
# for unequal iterables zip cuts values of larger iterable
for a, b in zip(list, list[1:]):
    print(f"{a} {b}")
