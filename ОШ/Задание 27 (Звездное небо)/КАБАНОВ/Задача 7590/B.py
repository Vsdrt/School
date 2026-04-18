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


def getCluster(first_star):
	cluster = [star for star in stars if dist(first_star, star) < 0.6]

	if len(cluster) > 0:
		for star in cluster: stars.remove(star)
		next_cluster = [getCluster(star) for star in cluster]
		cluster += sum(next_cluster, [])

	return cluster



stars = [list(map(float, star.replace(",", ".").split())) for star in open("ОШ/Задание 27 (Звездное небо)/КАБАНОВ/Задача 7590/B.txt")]

print(len(stars))

clusters = []

while len(stars) > 0:
	first_star = stars.pop()
	cluster = [first_star] + getCluster(first_star)
	print(len(cluster))
	clusters += [cluster]

medoids = [medoid(cluster) for cluster in clusters]

px = 0
py = 0

px = sum(medoid[0] for medoid in medoids) / len(medoids)
py = sum(medoid[1] for medoid in medoids) / len(medoids)

print(abs(int(px * 10000)), abs(int(py * 10000)))
