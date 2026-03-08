print("x y z w")
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                    f = (not(z == x) and (y and x) or (not(w <= z) and (x <= y)))
                    if f == 0:
                    #if f == 0 and y==1 and w == 1:
                        print(x, y, z, w)

pprint("otvet: y x z w")
