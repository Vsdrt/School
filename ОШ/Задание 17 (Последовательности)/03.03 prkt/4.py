def per(x, n):
    s = ''
    while x > 0:
        s = str(x%n) + s
        x //= n
    return s



a = [int(x) for x in open("17_04.txt")]
res = []

for i in range(len(a) - 1):
    x = a[i:i+2]
    if str(per(abs(sum(x)), 5))[-2:] == "14" and str(x[0]).count("3") == 2:
        res += [sum(x)]

print(len(res), max(res))
