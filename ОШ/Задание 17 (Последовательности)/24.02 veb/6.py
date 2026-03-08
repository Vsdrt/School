from math import prod

f = open("17_6.txt")
a = [int(x) for x in f]
sm = sum(x for x in a if x%2!=0 and len(str(abs(x)))==5)

res= []

for i in range(len(a)-1):
    x = a[i:i+2]
    if sum(str(c)[-1] == str(sm)[-1] for c in x)==1:
        res += [prod(x)]

print(len(res), max(res))
