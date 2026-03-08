print("x y z w f")

for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                f = not(y <= x) or (z <= w) or not(z)

                if f == 0:
                    print(x, y, z, w, f)

print("otvet: y x z w")
