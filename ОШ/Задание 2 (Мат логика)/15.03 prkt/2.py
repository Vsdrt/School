print("x y z w")

for x in range(2):
	for y in range(2):
		for z in range(2):
			for w in range(2):

				vr = ((x or y) == (y <= z)) or w

				if vr == 0:
					print(x, y, z, w)