a = [int(x) for x in open("17_1.txt")]
res = []

for i in a:
    if (str(i)[-1] == "5" or str(i)[-1] == "7") and i%9!=0\
       and i%11!=0:
        res += [i]

print(len(res), min(res) + max(res))
    
