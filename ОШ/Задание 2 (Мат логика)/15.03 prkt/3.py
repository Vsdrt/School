print("x y z w")

for x in range(2):
	for y in range(2):
		for z in range(2):
			for w in range(2):

				q = (x or y or z) <= (x and (y or w))

				if not(q):
					print(x, y, z, w)