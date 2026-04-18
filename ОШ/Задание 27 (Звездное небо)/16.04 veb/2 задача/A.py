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


stars = [list(map(float, star.replace(",", ".").split())) for star in open("A.txt")]

n = 3
clusters = {
	1: [],
	2: [],
	3: []
}

for star in stars:
	x, y = star

	if x > 5 and y > 5:
		clusters[1] += [star]
	elif x < 5 and  y > 5:
		clusters[2] += [star]
	else:
		clusters[3] += [star]

print(len(stars), len(clusters[1]), len(clusters[2]), len(clusters[3]))

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

print(int(px / n * 100_000), int(py / n * 100_000))