cnt = 0

for s in open("9_02.txt"):
    a = sorted([int(x) for x in s.split()])
    
    if ((a[0])**2 + (a[1])**2 + (a[2])**2) > (a[3] * a[4] * a[5]):
        cnt += 1

print(cnt)
        
    
