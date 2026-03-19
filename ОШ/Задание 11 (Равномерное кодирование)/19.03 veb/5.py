from math import log2, ceil


i = ceil(log2(10 + 52 + 458))

for k in range(1, 14543):
    ID = ceil(k * i / 8)

    if ID * 862 <= 276 * 1024:
        print(k)
