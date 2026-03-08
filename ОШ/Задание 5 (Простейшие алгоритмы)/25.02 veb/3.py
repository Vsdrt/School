def f(n):
    s = bin(n)[2:]

    if n%2 == 0:
        s = s + "0"
    else:
        s = s + "1"

    if s.count("1")%2 != 0:
        s = s + "1"
    else:
        s = s + "0"

    return int(s, 2)

print(bin(f(13)))
print(bin(f(10)))

res = []
for n in range(1, 1000):
    if f(n) > 2023:
        res.append(f(n))

print(min(res))
