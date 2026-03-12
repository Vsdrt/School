from ipaddress import *

net = ip_network(f"172.16.168.0/255.255.248.0", 0)

k = 0
for x in net:
	s = f"{x:b}"
	if s.count("1")%5!=0:
		k += 1

print(k)