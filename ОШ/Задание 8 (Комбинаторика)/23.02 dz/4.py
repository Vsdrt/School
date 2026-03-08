from itertools import product

s = "видео"
gl = set("иое")
res = set()
for x in product(s, repeat = 6):
    a = "".join(x)

    if a.count("и") >= 1 and a.count("е") >= 1:
        vowels = [c for c in a if c in gl]
        ok = True
        for i in range(len(vowels) - 1):
            if vowels[i] > vowels [i + 1]:
                ok = False
                break
        if ok:
            res.add(a)
        
print(len(res))



    

