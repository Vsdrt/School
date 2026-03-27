from math import ceil, log2


id = ceil(200 * ceil(log2(10 + 2040)) / 8)

print((id * 98304) // 1024 )