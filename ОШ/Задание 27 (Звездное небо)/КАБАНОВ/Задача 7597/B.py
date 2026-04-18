def dist(star_1, star_2):
	x1, y1 = star_1
	x2, y2 = star_2
	return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5


# АЛГОРИТМ DBSCAN
def getCluster(first_star): # звезда first_star, с которой начинается "рост" кластера

	# из глобального списка stars выбираются все звезды, находящиеся на расстоянии меньше 1 от first_star. Они попадают в список cluster
	# ВАЖНО: звезда first_star тоже попадет в cluster, тк dist(first_star, first_star) = 0 < 1
	cluster = [star for star in stars if dist(first_star, star) < 0.1] 
	
	# Если в радиусе 1 нашлась хотя бы одна звезда (а она всегда найдётся — как минимум сама first_star), то эти звезды удаляются из общего списка stars.
	# Это делается, чтобы каждая звезда была обработана ровно один раз и не попала в другой кластер
	if len(cluster) > 0:
		for star in cluster: stars.remove(star)
		
		# Для каждой звезды , которая оказалась соседкой first_star (т.е. попала в cluster), мы рекурсивно вызываем getCluster(star).
		# Каждый такой вызов вернёт новый список звезд, которые находятся на расстоянии < 1 от звезды и ещё не были удалены из stars (потому что предыдущие уже удалены)
		next_cluster = [getCluster(star) for star in cluster]

		# Мы берём исходный cluster (соседи first_star) и добавляем к нему все звезды из всех рекурсивно найденных соседей
		cluster = cluster + sum(next_cluster, [])

	# Возвращаем готовый кластер (список всех звёзд, связанных через цепочку соседей с first_star)
	return cluster


def medoid(cluster):
	m = []

	for star_1 in cluster:
		sm = sum(dist(star_1, star_2) for star_2 in cluster)
		m.append([sm, star_1])
	
	return min(m)[1]


f = open("ОШ/Задание 27 (Звездное небо)/КАБАНОВ/Задача 7597/B.txt")

stars = []

for s in f:
	s = s.replace(",", ".")
	star = [float(c) for c in s.split()]
	stars += [star]

print(len(stars))

clusters = []

while len(stars) > 0:
	first_star = stars.pop() # берем первую попавшуюся точку за начало кластера
	cluster = [first_star] + getCluster(first_star)
	print(len(cluster))
	clusters += [cluster]

k = len(clusters)
medoids = [medoid(cluster) for cluster in clusters]
print(medoids)

px = 0
py = 0

for medoid in medoids:
	px += medoid[0]
	py += medoid[1]

print(int(px / k * 10000), int(py / k * 10000))