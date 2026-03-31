from math import ceil


T = 5 * 60 # sec
k = 4
F = 40 * 1000 # hz
i = 16 # bit 

I = T * k * F * i # bit

print(ceil(I / 8 / 1024 / 1024))