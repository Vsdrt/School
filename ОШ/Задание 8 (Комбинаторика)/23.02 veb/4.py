from itertools import product

s = "0123456789abcdef"
res = set()
for x in product(s, repeat = 3):
    a = "".join(x)
    a1 = [x for x in a if a.count(x) == 1]

    if len(a1) == 3 and a[0] != "0" and ((int(a[0], 16)%2 == 0 and int(a[1], 16)%2 != 0 and int(a[2], 16)%2 == 0) \
    or (int(a[0], 16)%2 != 0 and int(a[1], 16)%2 == 0 and int(a[2], 16)%2 != 0)):
        res.add(x)

print(len(res))
