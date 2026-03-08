from itertools import product

s = "0123456789abcdefg"
res = set()



for x in product(s, repeat = 5):
    a = "".join(x)

    if a[0]!= "0" and a.count("b") == 1 and a.count("g") >= 1 and\
       ((int(a[0], 17)%2==0 and int(a[1], 17)%2!=0 and int(a[2], 17)%2==0 and int(a[3], 17)%2!=0 and int(a[4], 17)%2==0) or\
        (int(a[0], 17)%2!=0 and int(a[1], 17)%2==0 and int(a[2], 17)%2!=0 and int(a[3], 17)%2==0 and int(a[4], 17)%2!=0)):
        res.add(a)

print(len(res), res)
