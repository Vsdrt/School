def solve(n):

    s = bin(n)[2:]

    if n % 3 == 0:
        s = s + s[-3:]
    else:
        s = s + bin(3*(n%3))[2:]

    return int(s, 2)


mx = 0
n_mx = 0

for n in range(1, 10000):
    if solve(n)  < 100:
        #print(n, solve(n))
        print(n)


