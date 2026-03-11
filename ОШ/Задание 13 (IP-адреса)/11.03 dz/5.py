from ipaddress import *



net = ip_network(f"119.124.96.0/255.255.240.0", 0)

k = 0
for x in net:
	s = f"{x:b}"
	if s[-1] == "0":
		k += 1

print(k)