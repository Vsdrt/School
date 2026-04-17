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


stars = [list(map(float, star.replace(",", ".").split())) for star in open("ОШ/Задание 27 (Звездное небо)/14.04 dz/4 задача/B.txt")]

n = 3
clusters = {
	1: [],
	2: [],
	3: []
}

for star in stars:
	x, y = star

	if x < 0:
		clusters [1] += [star]
	elif y > 8:
		clusters[2] += [star]
	else:
		clusters[3] += [star]

print(len(stars))
print(len(clusters[1]), len(clusters[2]), len(clusters[3]))
print(len(clusters[1]) + len(clusters[2]) + len(clusters[3]))

medoids = [
	medoid(clusters[1]),
	medoid(clusters[2]),
	medoid(clusters[3])
]

print(medoids)

px = 0
py = 0

for medoid in medoids:
	px += medoid[0]
	py += medoid[1]

print(abs(int(px / n * 10_000)), abs(int(py / n * 10_000)))