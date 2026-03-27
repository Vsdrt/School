from math import ceil, log2

k = 8
i = ceil(log2(10))
ser = k * i 


k = 2
i = ceil(log2(18)) 
p_and_p = k * i 

id = ceil((p_and_p + ser) / 8)

print(25 * id)