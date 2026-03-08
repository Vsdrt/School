def f(x, a):
    return x%12==0 and 70 <= x <= 80 and x%a!=0

a = 0
while True:
     a += 1
     if all(not f(x, a) for x in range(1, 10000)):
         print(a)
