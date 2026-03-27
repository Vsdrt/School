from math import ceil, log2

len = 5
i = ceil(log2(10 + 7084))

ID = ceil(i * len / 8)

print(ID * 22528 // 1024)
