import itertools

for a, b, c in itertools.product ("0123", repeat = 3):
    x1 = int(f"13{a}{b}22{c}", 4)

    for d, e in itertools.product ("01234567", repeat = 2):
        x2 =int(f"1{d}{e}50", 8)

        for f in "123456789abcdef":
            x3 =int(f"{f}c28", 16)

            if x1 == x2 ==x3:
                print(x1)
