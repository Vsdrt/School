from math import log2


i_1 = int(log2(26)) + 1
k_1 = 12
i_2 = int(log2(5000)) + 1

id = (i_1 * k_1) + (i_2)
id = int(id /8 ) + 1

polz = 1020 / 60
print(polz - id)
