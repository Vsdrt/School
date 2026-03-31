I = 3840 * 2160 * 24
dop = 120 * 1024 * 8
I_szh =  I * 0.65 + dop 
I_karta = 20 * 1024 * 1024 * 1024 * 8
V = I_szh * 4320 

k = 0

while True:
	if V <= 0:
		break

	V = V - I_karta
	k += 1

print(k)

	