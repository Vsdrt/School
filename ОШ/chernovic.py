stroka = "s"*40 + "k"*28

for i in range(20000):
	stroka = stroka.replace("kk", "s", 1)
	stroka = stroka.replace("ss", "kkkk", 1)
	stroka = stroka.replace("sk", "kkk", 1)
	if len(stroka) == 85:
		print(stroka.count("s"))
		break