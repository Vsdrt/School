def dist(star1, star2):
	x1, y1 = star1
	x2, y2 = star2
	return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5


def medoid(cluster):
	sum_res = 10 ** 20

	for star1 in cluster:
		sum_star1 = 0

		for star2 in cluster:
			sum_star1 += dist(star1, star2)

		if sum_star1 < sum_res:
			sum_res = sum_star1

			res = star1

	return res


stars = []

for star in open("ОШ/Задание 27 (Звездное небо)/14.04 dz/1 задача/A.txt"):
	star = star.replace(",", ".")
	star = [float(x) for x in star.split()]
	stars += [star]

print(len(stars))

clusters = {
	1: [],
	2: []
}

for star in stars:
	x, y = star

	if y > 8:
		clusters [1] += [star]
	else:
		clusters [2] += [star]

for cluster in clusters:
	print(cluster, len(clusters[cluster]))


medoids = [
	medoid(clusters[1]),
	medoid(clusters[2]),
]

px = 0
py = 0

for medoid in medoids:
	px += medoid[0] 
	py += medoid[1]

print(int(px / 2 * 10000), int(py / 2 * 10000))



