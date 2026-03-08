def per(x, n):
    s = ''
    while x > 0:
        s = str(x%n) + s
        x //= n
    return s
    

a = [int(x) for x in open("17_01.txt")]

res = []

for i in range(len(a) - 2):
    x = a[i:i+3]
    if sum(str(per(c, 3))[-1]=="2" for c in x)>=1:
        res += [min(x)]

print(len(res), sum(res))
