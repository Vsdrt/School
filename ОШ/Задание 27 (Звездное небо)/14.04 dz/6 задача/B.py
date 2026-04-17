from math import dist



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


stars = [list(map(float, star.replace(",", ".").split())) for star in open("ОШ/Задание 27 (Звездное небо)/14.04 dz/6 задача/B.txt")]

n = 4
clusters = {
	1: [],
	2: [],
	3: [],
	4: []
}

for star in stars:
	x, y = star

	if y < - 4 * x + 44:
		clusters[1] += [star]
	elif y > 3.5 * x - 31 and y > - 4 * x + 44:
		clusters[2] += [star]
	elif y < 3.5 * x - 31 and y > x / 3:
		clusters[3] += [star]	
	else:
		clusters[4] += [star]

print(len(stars), len(clusters[1]), len(clusters[2]), len(clusters[3]), len(clusters[4]))
print(len(clusters[1]) + len(clusters[2]) + len(clusters[3]) + len(clusters[4]))

medoids = [
	medoid(clusters[1]),
	medoid(clusters[2]),
	medoid(clusters[3]),
	medoid(clusters[4])
]

print(medoids)

px = 0
py = 0

for medoid in medoids:
	px += medoid[0]
	py += medoid[1]

print(int(px / n * 10_000), int(py / n * 10_000))