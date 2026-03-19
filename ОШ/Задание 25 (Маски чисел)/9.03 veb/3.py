from itertools import product


def prost(x):
    if x == 0 or x == 1:
        return False
    for i in range(2, int(x**0.5) + 1):
        if x % i == 0:
            return False
    return True


cif = "0123456789"
res = set()

for a in cif:
    for d in cif:
        for k in range(4):
            for p in range(4 - k):
                for b in product(cif, repeat=k):
                    for c in product(cif, repeat=p):
                        b = "".join(b)
                        c = "".join(c)
                        x = f"1{a}2{b}0{c}2{d}1"
                        x = int(x)
                        if x <= 10**10 and int(x**0.5) == x**0.5:
                            if prost(int(x**0.5)):
                                res.add(x)
for x in sorted(res):
    print(x)
