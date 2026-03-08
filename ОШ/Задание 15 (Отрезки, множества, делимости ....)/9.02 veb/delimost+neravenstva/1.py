def f(x, a):
    return (a % 9) == 0 and ((280 % x == 0) <= ((a % x != 0) <= (730 % x != 0)))


a = 0
while True:
    a += 1
    if all(f(x, a) for x in range(1, 10001)):
       print(a)
       break
    
print("otvet: 90")
