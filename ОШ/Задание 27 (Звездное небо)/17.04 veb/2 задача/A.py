def dist(a, b):
	x1, y1 = a
	x2, y2 = b
	return ((x2 - x1)**2 + (y2 - y1)**2)**0.5


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


def getCluster(first_star):
	cluster = [star for star in stars if dist(first_star, star) < 0.5]

	if len(cluster) > 0:
		for star in cluster: stars.remove(star)
		next_cluster = [getCluster(star) for star in cluster]
		cluster = cluster + sum(next_cluster, [])

	return cluster


f = open("A.txt")

r, k = f

stars = [list(map(float, star.replace(",", ".").split())) for star in f]
print(len(stars))

clusters = []

while len(stars) > 0:
	first_star = stars.pop()
	cluster = [first_star] + getCluster(first_star)
	if len(cluster) < 10:
		continue
	print(len(cluster))
	clusters += [cluster]

medoids = []

for cluster in clusters:
	medoids = medoids + [medoid(cluster)]

print(medoids)

print(int(medoid(medoids)[0] * 10_000), int(medoid(medoids)[1] * 10_000))
