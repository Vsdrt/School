from itertools import product

s = "timahevsk"
res = set()
for x in product(s, repeat = 6):
    a = "".join(x)

    if (a.count("i") + a.count("a") + a.count("e")\
        < a.count("t") + a.count("m") + a.count("h") + a.count("v") + a.count("s") + a.count("k"))\
       and ("th" not in a and "mh" not in a and "hh" and "vh" not in a and "sh" not in a and "kh" not in a \
        and "ht" not in a and "hm" not in a and "hh" and "hv" not in a and "hs" not in a and "hk" not in a):
        res.add(x)


print(len(res))
