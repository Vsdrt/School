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

n = 2
clusters = {
	1: [],
	2: []
}

for star in stars:
	x, y = star

	if y > -1 and x < 1:
		clusters[1] += [star]
	elif y < -1 and x > 0:
		clusters[2] += [star]


# АЛГОРИТМ УДАЛЯЕТ ТОЛЬКО ОДИНОЧНЫЕ АНОМАЛИИ

# руками добавляем аномалию в исходный файл, чтобы удостовериться, что чистка работает
print(len(clusters[1]), len(clusters[2]))

for cluster in clusters: # удаляем аномалии
    clusters[cluster] = [star_1 for star_1 in clusters[cluster] for star_2 in clusters[cluster] if any(dist(star_1, star_2)) < 1 and star_1 != star_2]   # не сравниваем с самой собой

print(len(clusters[1]), len(clusters[2]))

medoids = [
	medoid(clusters[1]),
	medoid(clusters[2])
]

px = 0
py = 0

for medoid in medoids:
	px += medoid[0]
	py += medoid[1]

print(int(px / n * 100_000), int(py / n * 100_000))