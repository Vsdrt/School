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



stars = [list(map(float, star.replace(",", ".").split())) for star in open("ОШ/Задание 27 (Звездное небо)/16.04 dz/3 задача/B.txt")]

print(len(stars))

clusters = {
	1: [],
	2: [],
	3: [],
	4: [],
	5: []
}

for star in stars:
	x, y = star

	if y > 2 and x > -1:
		clusters[1] += [star]
	elif y > 2 and x < -1:
		clusters[2] += [star]
	
	elif y < 2 and x > 0:
		clusters[3] += [star]
	elif y < 2 and x > -3 and x < 0:
		clusters[4] += [star]
	else:
		clusters[5] += [star]


print(len(clusters[1]), len(clusters[2]), len(clusters[3]), len(clusters[4]), len(clusters[5]))

krais = [
	krai(clusters[1]),
	krai(clusters[3]),
	krai(clusters[4]),
	krai(clusters[5])
]

print(krais)

tx = sum(krai[0] for krai in krais) / 4
ty = sum(krai[1] for krai in krais) / 4

print(int(tx * 10_000), int(ty * 10_000))