from math import ceil, log2


# личный код
i_lkod = ceil(log2(15 * 2))
L_KOD = ceil(18 * i_lkod / 8)

# код подразделения  
i_kod_podr = ceil(log2(900))
KOD_PODR = ceil(i_kod_podr / 8)

print(30 - KOD_PODR - L_KOD)