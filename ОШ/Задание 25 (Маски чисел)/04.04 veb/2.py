from itertools import product



cif = "0123456789"
res = set()

for b in cif:
    for c in cif:
        for k in range(4): 
            for a in product(cif, repeat = k):
                a = "".join(a)
                x = "1" + a + "2" + b + c + "76"
                x = int(x)
                if x <= 10**8 and x%1923 == 0:
                    res.add(x)

for x in sorted(res):
    print(x, x//1923)
