a = [int(x) for x in open("17_11.txt")]
res = []

for i in a:
    if i%3==0 and i%11==0 and (str(i)[-1] == "2" or str(i)[-1] == "7"):
        res += [i]

print(len(res), min(res), res)





