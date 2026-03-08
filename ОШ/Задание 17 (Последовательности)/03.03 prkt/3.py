from math import prod


def solve(x):
    x = list(set(sorted(str(x))))
    x.sort()

    if len(x) == 10:
        return True
    else:
        return False
            

a = [int(x) for x in open("17_03.txt")]
des = [0,1,2,3,4,5,6,7,8,9]
sm = sum(x for x in a)
res = []

for i in range(len(a) - 2):
    x = a[i:i+3]
    if solve(prod(x)) and sum(x) < sm:
        res += [sum(x)]

print(len(res), min(res))
