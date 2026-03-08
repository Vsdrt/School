s = list("2"*323 + "0"*115 + "1"*562)


for i in range(len(s)):
    if s[i] == "0":
        s[i] = 2
    elif s[i] == "1":
        s[i] = "0"
        break
    elif s[i] == "2":
        s[i] = "1"

print(sum(map(int, s)))


        
