print("x y z w")
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                f = ((x <= y) and (z or w)) <= ((x == w) or (y and not(z)))
                if not f:
                    print(x, y, z, w)
print("otvet: y x w z")
