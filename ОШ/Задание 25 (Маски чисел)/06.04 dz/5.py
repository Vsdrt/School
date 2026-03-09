def prost(x):
	if x == 1:
		return False
	for i in range(2, int(x**0.5) + 1):
		if x%i==0:
			return False
	return True


for x in range(9_999_800, 10_000_500):
	if prost(x):
		print(abs(10_000_000 - x), x)