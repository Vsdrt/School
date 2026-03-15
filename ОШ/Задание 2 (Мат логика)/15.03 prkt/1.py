print("x y z w")

for x in range(2):
	for y in range(2):
		for z in range(2):
			for w in range(2):

				vr = ((y and (x == (not(z)))) <= w) and (z <= y)

				if vr == 0:
					print(x, y, z, w)