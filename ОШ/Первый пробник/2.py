print("z y x w")
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                q = (x or y) and not(y == z) and not(w)

                if q:
                    print(z, y, x, w)
    
