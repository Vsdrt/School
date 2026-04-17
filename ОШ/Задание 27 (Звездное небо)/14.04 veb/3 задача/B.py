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

n = 3
clusters = {
	1: [],
	2: [],
	3: []
}

for star in stars:
	x, y = star

	if x > 5 and y > 13.5 - x:
		clusters [1] += [star]
	elif x < 5 and y > x + 3:
		clusters [2] += [star]
	else:
		clusters [3] += [star]

print(len(clusters[1]) + len(clusters[2]) + len(clusters[3]))
print(len(stars))

medoids = [
	medoid(clusters[1]),
	medoid(clusters[2]),
	medoid(clusters[3])
]

px = 0
py = 0

for medoid in medoids:
	px += medoid[0]
	py += medoid[1]

print(int(px / n * 10_000), int(py / n * 10_000))