a = [int(x) for x in open("17_04.txt")]
res = []

for i in a:
    if i > 100 and int(str(i)[-2]) <= 4 and 3 <= int(str(i)[-3]) <= 7:
        res += [i]

print(len(res), min(res))
