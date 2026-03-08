def per(x):
    s = ""
    while x > 0:
        s = s + str(x%3)
        x //= 3
    return s


f = open("17_8.txt")
a = [int(x) for x in f]
res = []

for i in range(len(a) - 2):
    x = a[i:i+3]
    if sum(per(c)[-1] == "2" for c in x)>=1:
        res += [min(x)]

print(len(res), sum(res))
