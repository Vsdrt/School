from ipaddress import *


net = ip_network(f"117.32.0.0/255.224.0.0", 0)

k = 0

for x in net:
	b = str(x).split(".")

	if len(set(b)) == 3:
		k += 1

print(k-2)