from math import ceil, log2


kod = ceil(11 * ceil(log2(13 + 10 + 5)) / 8)
dop = 12

print(ceil((dop + kod) * 198 / 1024))