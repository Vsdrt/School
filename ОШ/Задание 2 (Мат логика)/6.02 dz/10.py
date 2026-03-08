print("x y z w")
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                f = not(y <= w) or (x <= z) or not(x)
                if not f:
                    print(x, y, z, w)

print("otvet: x y w z")
