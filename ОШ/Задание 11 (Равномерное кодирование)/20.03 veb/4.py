from math import ceil, log2

k = 26
i = ceil(log2(26))
par = k * i

k = 3
i = ceil(log2(10))
id = k * i

polz = id + par 

print(ceil(polz * 38776 / 8  / 1024))

