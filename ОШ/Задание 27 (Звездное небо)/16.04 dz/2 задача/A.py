def dist(a ,b):
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


stars = [list(map(float, star.replace(",", ".").split())) for star in open("ОШ/Задание 27 (Звездное небо)/16.04 dz/2 задача/A.txt")]

n = 2
clusters = {
	1: [],
	2: []
}

for star in stars:
	x, y = star

	if y > 2 and x > 1 and x < 6.5:
		clusters[1] += [star]
	elif y < 2:
		clusters[2] += [star]

print(len(stars), len(clusters[1]), len(clusters[2]))

medoids = [
	medoid(clusters[1]),
	medoid(clusters[2])
]

print(medoids)

px = 0
py = 0

for medoid in medoids:
	px += medoid[0]
	py += medoid[1]

print(int(px / n * 100_000), int(py / n * 100_000))