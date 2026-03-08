print("x y z w")
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                f = x and not(y) and (not(z) or w)

                if f:
                    print(x, y, z, w)

print("otvet: z y x w")
