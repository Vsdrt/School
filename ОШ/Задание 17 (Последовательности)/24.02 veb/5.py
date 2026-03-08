f = open("17_5.txt")
a = [int(x) for x in f]
mx = max(c for c in a if str(c)[-2:] == "25")

res = []

for i in range(len(a) - 2):
    x = a[i:i+3]

    if sum(len(str(abs(c)))==4 for c in x)<=2 and sum(x)<= mx:
        res += [sum(x)]

print(len(res), max(res))
    
