def f(n):
    s = bin(n)[2:]
    
    if n % 2 == 0:
        s = "1" + s + str(s.count("1")%2)
    else:
        s = s + "0" + str(s.count("1")%2)

    return int(s, 2)


f_min = 10000000000
n_min = 0

for n in range(1, 10000):
     if f(n) > 100:
         if f_min > f(n):
             f_min = f(n)
             n_min = n

print(f_min, n_min)
