def dist(a, b):
	x1, y1 = a
	x2, y2 = b
	return ((x2 - x1)**2 + (y2 - y1)**2)**0.5


def md(cl):
	sum_res = 10 ** 20

	for a in cl:
		sum_a = 0
		for b in cl:
			sum_a += dist(a, b)

		if sum_a < sum_res:
			sum_res = sum_a
			res = a
	
	return res


def rd(cl, md):
	dists = []

	for a in cl:
		dists += [dist(a, md)]

	return max(dists)


sts = [list(map(float, st.replace(",", ".").split())) for st in open("ОШ/Задание 27 (Звездное небо)/17.04 dz/3 задание/B.txt")]
print(len(sts))

cls = {
	1: [],
	2: [],
	3: [],
	4: [],
	5: []
}

for st in sts:
	x, y = st

	if y > 5:
		if x > 3:
			cls[1] += [st]
		else:
			cls[2] += [st]
	elif y > 2:
		if x > 2:
			cls[3] += [st]
		else:
			cls[4] += [st]
	else:
		cls[5] += [st] 


sm = 0
for cl in cls:
	sm += len(cls[cl])
	print(len(cls[cl]))
print(sm)

mds = []
for cl in cls:
	mds += [md(cls[cl])]
print(mds)

rds = [
	rd(cls[1], mds[0]),
	rd(cls[2], mds[1]),
	rd(cls[3], mds[2]),
	rd(cls[4], mds[3]),
	rd(cls[5], mds[4])

]
print(rds)

print(int(min(rds) * 10_000), int(max(rds) * 10_000))