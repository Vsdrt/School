a = [int(x) for x in open("17_05.txt")]
res = []


for x in range(len(a) - 1):
    for y in range(x+1, len(a)):
        p = [x, y]
        if sum(p)%120 == 0:
            res += [sum(p)]

print(len(res), max(res))
        
