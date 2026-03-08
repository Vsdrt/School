res = set()
for y in range(9, 18):
    for x in range(y):
        a = int("500a", 18) + x*18**2 + y*18**1
        a += int("1807", y) + x*y **1
        res.add(a)

print(len(res))
