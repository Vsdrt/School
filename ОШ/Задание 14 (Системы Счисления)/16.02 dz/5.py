s = 0

for x in range(17):
    a = int("14903", 17) + x*17**1
    b = int("0612", 17) + x*17**3
    c = int("0540", 17)+ x*17**0 + x*17**3
    if (a+b-c)%7==0:
        s += x
print(s)


