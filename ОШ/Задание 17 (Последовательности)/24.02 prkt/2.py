def nod(x, y): #костыль, нужно делать вычитанием
    
    nod = set()
    for z in range(1, 10000): 
        if x%z==0 and y%z==0:
            nod.add(z)
    return max(nod)




f = open("17_2.txt")
a = [int(x) for x in f]
res = []

for i in range(len(a)-1):
    x = a[i:i+2]
    
    if sum(c%2==0 and c > 0 for c in x)==2 and nod(x[0], x[1]) > 100:
        res += [abs(x[0] - x[1])]

print(len(res), max(res))
