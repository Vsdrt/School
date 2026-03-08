f = open("17_4.txt")
a = [int(x) for x in f]
mx = max(x for x in a if str(x)[-2:] == "30")

res = []

for i in range(len(a) - 2):
    x = a[i:i+3]

    if sum(len(str(abs(c)))==4 for c in x) == 0 and sum(x) > mx:
        res += [sum(x)]

print(len(res), max(res))
