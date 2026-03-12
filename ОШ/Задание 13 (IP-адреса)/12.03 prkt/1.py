from ipaddress import *

net = ip_network("154.233.0.0/255.255.0.0", 0)

k = 0
for x in net:
	if bin(int(str(x)[-1]))[2:][-1] == "0":
		k += 1

print(k)