from math import floor


t = 1 * 1024 * 60 / 1.5
print(t)
I = (2 * 48000 * t * 24) / 8 / 1024 / 1024
I = 0.16 * I

print(I / 15)

