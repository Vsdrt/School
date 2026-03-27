from math import ceil, log2


len_L = 7
i_L = ceil(log2(26))
left = len_L * i_L

len_R = 4
i_R = ceil(log2(10))
right = len_R * i_R

polz = 2385 // 45

print(polz - ceil((left + right) / 8))
