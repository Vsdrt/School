def dist(a, b):
	x1, y1 = a
	x2, y2 = b
	return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5


def f(cluster_1, cluster_2):
	mn_res = 10**20
	mx_res = 0

	for a in cluster_1:
		for b in cluster_2:
			if dist(a, b) < mn_res:
				mn_res = dist(a, b)

			if mx_res < dist(a, b):
				mx_res = dist(a, b)

	return int(mn_res * 10_000), int(mx_res * 10_000)


stars = [list(map(float, star.replace(",",".").split())) for star in open("B.txt")]
print(len(stars))

n = 3
clusters = {
	1: [],
	2: [],
	3: []
}

for star in stars:
	x, y = star

	if y > 5 and x < 5.5:
		clusters[1] += [star]
	elif y < 5 and x < 5.5 and y > 1.5:
		clusters[2] += [star]
	elif y < 7 and x > 7.5 and y > 1.5:
		clusters[3] += [star]

print(len(clusters[1]), len(clusters[2]), len(clusters[3]))

print(
	f(clusters[1], clusters[2]),
	f(clusters[1], clusters[3]),
	f(clusters[2], clusters[3])
	)
