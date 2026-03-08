def f(x, y, a):
    return ((x + a > 180) <= (a&36 ==0)) or ((y%12==0) and (x&36!=0))

for a in range(100, 1, -1):
    if all(f(x, y, a) for x in range(1000) for y in range(1000)):
        print(a)
        break
