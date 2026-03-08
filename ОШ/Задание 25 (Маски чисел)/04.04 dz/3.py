from itertools import product


cif = "0123456789"
res = set()

for a in cif:
    for b in cif:
        for c in cif:
            x = "2" + a + "34" + b + "56" + c + "8"
            x = int(x)
            if x <= 10**9 and x%151==0:
                res.add(x)

for x in sorted(res):
    print(x, x//151)
