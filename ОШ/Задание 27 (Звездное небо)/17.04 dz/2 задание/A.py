def dist(a, b):
	x1, y1 = a
	x2, y2 = b
	return max(abs(x2 - x1), abs(y2 - y1))


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


stars = [list(map(float, star.replace(",", ".").split())) for star in open("ОШ/Задание 27 (Звездное небо)/17.04 dz/2 задание/A.txt")]
print(len(stars))

clusters = {
	1: [],
	2: []
}

for star in stars:
	x, y = star

	if x > 3:
		clusters[1] += [star]
	else:
		clusters[2] += [star]

for cluster in clusters:
	print(len(clusters[cluster]))

medoids = []

for cluster in clusters:
	medoids += [medoid(clusters[cluster])]

k = len(clusters)
print(medoids)

px = 0
py = 0

for medoid in medoids:
	px += medoid[0]
	py += medoid[1]

print(int(px / k * 10_000), int(py / k * 10_000))