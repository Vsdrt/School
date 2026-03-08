mn = 10**10

for x in range(0, 8):
    for y in range(0, 8):
        a = int(f"36{x}53", 8)
        b = int(f"4{y}3", 8)
        if a - b > 0:
            if a - b < mn:
                mn = a - b
                
print(mn)

for x in range(0, 8):
    for y in range(0, 8):
        a = int(f"36{x}53", 8)
        b = int(f"4{y}{y}3", 8)
        if a - b > 0:
            if a - b < mn:
                mn = a - b
                
print(mn)

