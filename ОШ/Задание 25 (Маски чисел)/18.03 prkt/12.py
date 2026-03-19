from itertools import product


cif = "0123456789"

for x in range(1, 1000000):
    x = str(x)
    if (
        x[0] != "0"
        and int(x) % 103 == 0
        and all(int(x[p]) < int(x[p + 1]) for p in range(len(x) - 1))
    ):
        print(x, int(x) // 103)
