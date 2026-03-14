from itertools import combinations

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# Все простые числа ≤ 300
primes = [p for p in range(2, 301) if is_prime(p)]

results = []
for comb in combinations(primes, 4):
    prod = comb[0] * comb[1] * comb[2] * comb[3]
    if prod > 10**10:
        continue
    s = str(prod)
    # условие маски *5*3: число оканчивается на 3 и содержит цифру 5
    if s[-1] == '3' and '5' in s:
        results.append((prod, comb))

# Сортируем по возрастанию числа
results.sort()
min_num, min_factors = results[0]
max_num, max_factors = results[-1]

# Упорядочиваем множители
min_sorted = sorted(min_factors)
max_sorted = sorted(max_factors)

# Произведения
p_min = min_sorted[0] * min_sorted[3]      # наименьший * наибольший для минимального числа
p_max = max_sorted[1] * max_sorted[2]      # второй и третий для максимального числа

answer = p_min * p_max
print(answer)



