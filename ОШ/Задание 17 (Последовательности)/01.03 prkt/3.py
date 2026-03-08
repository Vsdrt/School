a = [int(x) for x in open("17_3.txt")]
res = []

for i in a:
    if i%3==0 and i%7!=0 and i%17!=0 and i%19!=0 and i%27!=0:
        res += [i]

print(len(res), max(res))
