def f(x, a):
    return ((x%a == 0) and (x%24==0) and (x%16!=0)) <= (x%a!=0)

a = 0
while True:
    a+=1
    if all(f(x/10, a) for x in range(1, 100000*10)):
        print(a)
        break
