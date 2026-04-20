def dist(a, b):
	x1, y1 = a
	x2, y2 = b
	return ((x2 - x1)**2 + (y2 - y1)**2) ** 0.5


def pl(cluster):
	sum_sosed = 0

	for star_1 in cluster:
		for star_2 in cluster:
			if dist(star_1, star_2) <= 1:
				sum_sosed += 1

	return sum_sosed / len(cluster)


stars = [list(map(float, star.split())) for star in open("ОШ/Задание 27 (Звездное небо)/17.04 dz/1 задание/B.txt")]
print(len(stars))

clusters = {
	1: [],
	2: [],
	3: [],
	4: [],
	5: [],
	6: [],
	7: []
}

for star in stars:
	x, y = star

	if x > 6:
		if y > 0:
			clusters[1] += [star]
		else:
			clusters[2] += [star]
	
	elif 1 < x < 6:
		if y > 1:
			clusters[3] += [star]
		else:
			clusters[4] += [star]
	
	elif -4 < x < 1:
		if y > -2.5:
			clusters[5] += [star]
		else:
			clusters[6] += [star]

	else:
		clusters[7] += [star]

for cluster in clusters:
	print(len(clusters[cluster]))

pls = [
	pl(clusters[1]),
	pl(clusters[2]),
	pl(clusters[3]),
	pl(clusters[4]),
	pl(clusters[5]),
	pl(clusters[6]),
	pl(clusters[7])
]

print(pls)

print(int(min(pls) * 100_000), int(sum(pls) / len(pls) * 100_000))