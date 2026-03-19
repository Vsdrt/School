from itertools import product


cif = "0123456789"
res = set()


for b in cif:
    for k in range(6):
        for a in product(cif, repeat=k):
            a = "".join(a)
            x = f"2{a}1234{b}6"
            x = int(x)
            if x <= 10**8 and x % 37 == 0:
                res.add(x)

for x in sorted(res):
    print(x, x // 37)
