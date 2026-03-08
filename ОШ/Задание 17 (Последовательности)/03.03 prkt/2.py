from math import prod


a = [int(x) for x in open("17_02.txt")]
sm = sum(int(str(abs(x))[0]) for x in a)
res = []

for i in range(len(a) - 1):
    x = a[i:i+2]
    if prod(x) > sm:
        res += [sum(x)]

print(len(res), max(res))
    
