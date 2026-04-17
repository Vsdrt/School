for x in range(22):
	a = int("8293402", 21) + x*21**1
	b = int("2924007", 21) + x*21**1 + x*21**2
	c = int("6756408", 21) + x*21**1

	if (a+b+c) % 20 == 0:
		print((a+b+c) // 20)
		break
