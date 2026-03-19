def per(x, n):
	s = ""
	while x > 0:
		s = str(x % n) + s
		x //= n
	return s


k = 0

for x in range(1, 17000):
    if len(per(x, 5)) <= 4:
        if len(bin(x)[2:]) >= 5:
            if hex(x)[2:][-1] == "c":
                print(per(x, 5), bin(x)[2:], hex(x)[2:])
                k += 1

print(k)

	

