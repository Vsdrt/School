from itertools import permutations

s = "01234567"
res = set()
ch = "0246"
nch = "1357"

for x in permutations(s, r = 5):
    a = "".join(x)

    if "1" not in a and a[0] != "0" and ((a[0] in ch and a[1] in nch and a[2] in ch and a[3] in nch and a[4] in ch)\
                                         or (a[0] in nch and a[1] in ch and a[2] in nch and a[3] in ch and a[4] in nch)):
        res.add(a)

print(len(res))
