from math import ceil, log2


k = 5
i = ceil(log2(23 + 10))
kod = ceil(k * i / 8)


nom = ceil(log2(299 - 100 + 1) / 8)


print(56 - nom - kod)