from math import ceil, log2

k = 5
i = ceil(log2(26))
ch1 = k * i

ch2 = ceil(log2(3000))

id = ceil((ch2 + ch1) / 8)

polz = 936 // 52
print(polz - id )
