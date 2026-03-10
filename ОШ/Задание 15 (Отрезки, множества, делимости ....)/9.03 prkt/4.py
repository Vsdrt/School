def f(x):
	return (x in {2, 4, 8, 12, 15}) <= ((x not in {3, 6, 8, 15}) or (x in a))


a = set()

for x in range(1, 100):
	if not f(x):
		print(x)

print(8*15)