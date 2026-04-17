def dist(a, b):
	x1, y1 = a
	x2, y2 = b
	return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5


def medoid(cluster):
	sum_res = 10 ** 20

	for a in cluster:
		sum_a = 0
		for b in cluster:
			sum_a += dist(a, b)

		if sum_a < sum_res:
			sum_res = sum_a
			res = a

	return res


stars = [list(map(float, star.replace(",", ".").split())) for star in open("ОШ/Задание 27 (Звездное небо)/14.04 dz/5 задача/B.txt")]

n = 6
clusters = {
	1: [],
	2: [],
	3: [],
	4: [],
	5: [],
	6: [],
}

for star in stars:
	x, y = star

	if y > 4 and y < x + 4:
		clusters[1] += [star]

	elif y < 4 and y < x - 2:
		clusters[2] += [star]

	elif y < 4 and y > x - 2 and y < x + 4:
		clusters[3] += [star]

	elif y > 7 and y < x + 12 and y > x + 4:
		clusters[4] += [star]

	elif y < 7 and y < x + 12 and y > x + 4:
		clusters[5] += [star]	
		
	else:
		clusters[6] += [star]

print(len(stars), len(clusters[1]), len(clusters[2]), len(clusters[3]), len(clusters[4]), len(clusters[5]), len(clusters[6]))
print( len(clusters[1]) + len(clusters[2])+len(clusters[3])+len(clusters[4])+len(clusters[5])+len(clusters[6]))

medoids = [
	medoid(clusters[1]),
	medoid(clusters[2]),
	medoid(clusters[3]),
	medoid(clusters[4]),
	medoid(clusters[5]),
	medoid(clusters[6]),
]

print(medoids)

px = 0
py = 0

for medoid in medoids:
	px += medoid[0]
	py += medoid[1]

print(int(px / n * 10000), int(py / n * 10000))