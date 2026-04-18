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


stars = [list(map(float, star.replace(",", ".").split())) for star in open("ОШ/Задание 27 (Звездное небо)/16.04 dz/1 задача/A.txt")]

print(len(stars))

n = 2
clusters = {
	1: [],
	2: []
}

for star in stars:
	x, y = star

	if y < 13 and x < 12 and y > -1:
		clusters[1] += [star]
	elif x > 12 and x < 28 and y > - x + 20:
		clusters[2] += [star]

print(len(clusters[1]), len(clusters[2]))

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

print(int(px / n * 10_000), int(py / n * 10_000))