from math import ceil, log2

k = 121
i = ceil(log2(52 + 9 + 16))
id = k * i

kod = ceil(log2(1024))

k = 500
i = ceil(log2(5000))
key = k * i 

polz = id + kod + key

print(int(512 * 1024 * 8 / polz))
