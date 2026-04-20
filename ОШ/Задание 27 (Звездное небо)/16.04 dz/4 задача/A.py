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


stars = [list(map(float, star.split())) for star in open("ОШ/Задание 27 (Звездное небо)/16.04 dz/4 задача/A.txt")]
print(len(stars))

n = 2
clusters = {
	1: [],
	2: []
}

for star in stars:
	x, y = star

	if y < -4*x/7 + 9 and x < 7 and y > 2:
		clusters[1] += [star]
	else:
		if x > 10 and y < 2:
			pass
		elif x < 2 and y < 2:
			pass
		else:
			clusters[2] += [star]

print(len(clusters[1]), len(clusters[2]))

medoids = [
	medoid(clusters[1]),
	medoid(clusters[2])
]

print(medoids)

px = sum(medoid[0] for medoid in medoids) / n
py = sum(medoid[1] for medoid in medoids) / n

print(int(px * 100_000), int(py * 100_000) )