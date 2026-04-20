def dist(a, b):
	x1, y1 = a
	x2, y2 = b
	return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5


def krai(cluster):
	sum_res = 0

	for a in cluster:
		sum_a = 0

		for b in cluster:
			sum_a += dist(a, b)

		if sum_a > sum_res:
			sum_res = sum_a
			res = a
			
	return res



stars = [list(map(float, star.replace(",", ".").split())) for star in open("ОШ/Задание 27 (Звездное небо)/16.04 dz/3 задача/A.txt")]

print(len(stars))

k = 3
clusters = {
	1: [],
	2: [],
	3: []
}

for star in stars:
	x, y = star

	if y > 0:
		clusters[1] += [star]
	elif x > 2:
		clusters[2] += [star]
	else:
		clusters[3] += [star]


print(len(clusters[1]), len(clusters[2]), len(clusters[3]))

krais = [
	krai(clusters[1]),
	krai(clusters[2])
]

print(krais)

tx = sum(krai[0] for krai in krais) / 2
ty = sum(krai[1] for krai in krais) / 2

print(int(tx * 10_000), int(ty * 10_000))