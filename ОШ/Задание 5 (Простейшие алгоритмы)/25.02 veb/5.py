def f(n):
    s = bin(n)[2:]

    if n % 3 == 0:
        s = s + s[-3:]
    else:
        s = s + bin(3*(n%3))[2:]

    return int(s, 2)



mn = 10**10

for n in range(1, 10000):
     if f(n) > 151:
         if f(n) < mn:
             mn = f(n)

print(mn)
         
