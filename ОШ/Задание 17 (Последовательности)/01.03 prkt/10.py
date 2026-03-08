def f(x):
    if x > 0 and str(x)[-1] == "9":
        return True
    else:
        return False
    

a = [int(x) for x in open("17_10.txt")]
res = []

for i in range(len(a)-2):
    x = a[i:i+3]
    if f(x[1]) == True and f(x[0]) == False and f(x[2]) == False:
        res += [sum(x)]

print(len(res), max(res))
