from itertools import product


cif = "0123456789"
res = set()


for k in range(6):
    for a in product(cif, repeat=k):
        a = "".join(a)
        x = f"1234{a}7"
        x = int(x)
        if x <= 10**8 and x % 141 == 0:
            res.add(x)

for i in sorted(res):
    print(i, i // 141)
