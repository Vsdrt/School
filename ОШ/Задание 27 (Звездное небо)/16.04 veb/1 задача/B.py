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


stars = [list(map(float, star.replace(",", ".").split())) for star in open("B.txt")]

n = 3
clusters = {
	1: [],
	2: [],
	3: []
}

for star in stars:
	x, y = star

	if x > 2 and y > -2 * x + 4 and y < 6:
		clusters[1] += [star]
	elif y < -2 * x + 4 and y < 3 and y > -1 and x < 1:
		clusters[2] += [star]
	elif x > 0 and y < 0 and y < x - 2:
		clusters[3] += [star]
	
print(len(clusters[1]), len(clusters[2]), len(clusters[3]))

medoids = [
	medoid(clusters[1]),
	medoid(clusters[2]),
	medoid(clusters[3]),
]

px = 0
py = 0

for medoid in medoids:
	px += medoid[0]
	py += medoid[1]

print(int(px / n * 100_000), int(py / n * 100_000))