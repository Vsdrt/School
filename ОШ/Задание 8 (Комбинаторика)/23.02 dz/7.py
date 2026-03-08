from itertools import permutations

s = "gleb ttd"
res = set()

for x in permutations(s):
    a = "".join(x)
    q = a.split(" ")
    s1 = q[0]
    s2 = q[1]

    if len(s1)>=1 and len(s2)>=1 and s1[0]!= "e" and s1[-1]!= "e" and s2[0]!= "e" \
       and s2[-1]!= "e" and a[0]!= " " and a[-1]!= " ":
        res.add(x)
print(len(res)-1, res)
