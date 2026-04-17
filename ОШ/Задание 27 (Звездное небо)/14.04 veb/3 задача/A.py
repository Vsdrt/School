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


stars = [list(map(float, star.replace(",", "."))) for star in open("A.txt")]

n = 2
clusters = {
	1: [],
	2: []
}

for star in stars:
	x, y = star

	if y > 4 - x:
		clusters [1] += [star]
	else:
		clusters [2] += [star]

print(len(clusters[1]) + len(clusters[2]))
print(len(stars))

medoids = [
	medoid(clusters[1]),
	medoid(clusters[2])
]

px = 0
py = 0

for medoid in medoids:
	px += medoid[0]
	py += medoid[1]

print(int(px / n * 10_000), int(py / n * 10_000))