def dist(a, b):
	x1, y1 = a
	x2, y2 = b
	return ((x2 - x1)**2 + (y2 - y1)**2)**0.5


def kr(cl):
	sum_res = 0

	for a in cl:
		sum_a = 0
		for b in cl:
			sum_a += dist(a, b)

		if sum_a > sum_res:
			sum_res = sum_a
			res = a

	return res


def getCluster(fst_st):
	cl = [st for st in sts if dist(st, fst_st) < 1]

	if len(cl) > 0:
		for st in cl: sts.remove(st)
		next_cl = [getCluster(st) for st in cl]
		cl = cl + sum(next_cl, [])

	return cl


sts = [list(map(float, st.replace(",", ".").split())) for st in open("ОШ/Задание 27 (Звездное небо)/17.04 dz/4 задание/B.txt")]
print(len(sts))

cls = []

while len(sts) > 0:
	fst_st = sts.pop()
	cluster = [fst_st] + getCluster(fst_st)
	if len(cluster) < 10:
		continue
	cls += [cluster]
	print(len(cluster))

krs = []

for cl in cls:
	krs += [kr(cl)]
print(krs)

tx = 0
ty = 0

for krai in krs:
	tx += krai[0]
	ty += krai[1]

print(int(tx * 10_000 / len(cls)), int(ty * 10_000 / len(cls)))

