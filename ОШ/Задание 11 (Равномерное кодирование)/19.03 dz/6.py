from math import ceil, log2


i = ceil(log2(26 + 450 + 10))

for len in range(1, 1000):
    nomer = ceil(len * i / 8)
    if 708 * nomer > 213 * 1024:
        print(len)
        break
