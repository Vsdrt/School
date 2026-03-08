def f(x, a):
    return (40 % a == 0) and (((x % a != 0) and (x % 54 == 0)) <= (x % 72 !=0))


a = 1000000

while True:
    a -= 1

    if all(f(x, a) for x in range(1, 10000)):
        print(a)
        break
    
print("otvet 8")
