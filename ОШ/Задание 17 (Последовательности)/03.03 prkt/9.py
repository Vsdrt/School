a = [int(x) for x in open("17_09.txt")]
mx = max(abs(x) for x in a if x%570==0)
res_4 = 0
res_3 = 0

for i in range(len(a) - 3):
    x = a[i:i+4]
    if sum(x)//4 > mx:
        res_4 += 1

for i in range(len(a) - 2):
    x = a[i:i+3]
    if sum(c > 0 for c in x) >= 2 and sum(x)%34==0:
        res_3 += 1

print(res_4, res_3)
                
    
