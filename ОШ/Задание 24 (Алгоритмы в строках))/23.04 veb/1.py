s = open("24_1.txt").readline()
print(s[:100])

# удаляем ненужные символы
for c in "6789":
	s = s.replace("c", 1)

# избавляемся от пар операций / разделяем строку
s = s.replace("-", "*")
s = s.replace("*", " ")

# избавляемся от незначащего нуля
s = s.replace("*01", " 1")
s = s.replace("*00", " 0")
s = s.replace(" 01", " 1")
s = s.replace(" 00", " 0")

# удаляем операции в начале и в конце
s = s.replace(" *", " ")
s = s.replace("* ", " ")

# находим ответ
for c in sorted(s.split(), key=len, reverse=1):
	print(len(c), c)
