print("x y z w")
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                f = (((not(z))) == (not(y))) or (not(x) and y) or w
                if not f:
                    print(x, y, z, w)

print("otvet: z x w y")
