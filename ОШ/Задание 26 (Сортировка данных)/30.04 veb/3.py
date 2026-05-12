f = open('26.txt')
n, k, m = map(int, f.readline().split())
a = [int(x) for x in f]
a.sort(reverse=True)
print(a[k + m])
print(sum(a[:k]) * 0.2 + sum(a[k:k+m]) * 0.1)