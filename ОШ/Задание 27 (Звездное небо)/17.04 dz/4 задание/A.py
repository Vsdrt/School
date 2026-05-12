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


sts = [list(map(float, st.replace(",", ".").split())) for st in open("ОШ/Задание 27 (Звездное небо)/17.04 dz/4 задание/A.txt")]
print(len(sts))

cls = {
	1: [],
	2: []
}

for st in sts:
	x, y = st

	if y < -x - 1 and y < x - 2:
		cls[1] += [st]
	elif y > -4 and y < x - 9 and y < -x + 11:
		cls[2] += [st]

for cl in cls:
	print(len(cls[cl]))

krs = [
	kr(cls[1]),
	kr(cls[2]),
]
print(krs)

tx = 0
ty = 0

for krai in krs:
	tx += krai[0]
	ty += krai[1]

print(int(tx * 10_000 / 2), int(ty * 10_000 / 2))

