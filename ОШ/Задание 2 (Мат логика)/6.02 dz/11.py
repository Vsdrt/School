print("x y z w")
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                f = not(w == y) and (z <= w) and not(x)
                if f:
                    print(x, y, z, w)

print("otvet: z x w y")
