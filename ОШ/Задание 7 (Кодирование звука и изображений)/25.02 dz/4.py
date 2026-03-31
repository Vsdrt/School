I = 3840 * 2160 * 24
k = 5922

karta = 8 * 1024 * 1024 * 1024 * 8
cnt = karta // I 

count = 0

while True:
	if k <= 0:
		break
	
	k = k - cnt
	count += 1

print(count)
	