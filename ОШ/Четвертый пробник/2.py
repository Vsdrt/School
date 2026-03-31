print("x y w z")

for x in range(2):
	for y in range(2):
		for z in range(2):
			for w in range(2):
				q = ((x <= y) == (y <= z)) and (y or w)

				if q == 1:
					print(x, y, w, z)