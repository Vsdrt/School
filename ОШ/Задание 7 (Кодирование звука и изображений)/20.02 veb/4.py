from math import log2

i = log2(4096)

photo = 1024 * 768 * i 

print(photo * 256 / 8 / 1024 / 1024)