from ipaddress import *



net = ip_network(f"105.224.200.224/255.255.255.224", 0)
k = 0

for i in net:
	s = f"{i:b}"
	if s.count("1")%4==0:
		k += 1

print(k)