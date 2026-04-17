def dist(star_1, star_2):
	x1, y1 = star_1
	x2, y2 = star_2
	return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5 


def medoid(cluster):
	sum_res = 10 ** 20

	for star_1 in cluster:
		sum_star = 0 

		for star_2 in cluster:
			sum_star += dist(star_1, star_2)

		if sum_star < sum_res:
			sum_res = sum_star
			res = star_1

	return res


stars = [list(map(float, star.replace(",", ".").split())) for star in open("ОШ/Задание 27 (Звездное небо)/14.04 dz/3 задача/A.txt")]

n = 4
clusters = {
	1: [],
	2: [],
	3: [],
	4: []
}

for star in stars:
	x, y = star

	if x > 16:
		clusters [1] += [star]
	elif y > 14:
		clusters [2] += [star]
	elif 10 < y < 14:
		clusters [3] += [star]
	else:
		clusters [4] += [star]

print(len(stars))
print(len(clusters[4]) + len(clusters[1]) + len(clusters[2]) + len(clusters[3]))

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