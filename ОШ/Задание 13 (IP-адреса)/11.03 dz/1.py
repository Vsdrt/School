from ipaddress import *

net = ip_network("174.114.120.0/255.255.252.0", 0)

k = 0
for x in net:
	s = f"{x:b}"
	if s.count("1")%2==0:
		k += 1

print(k)

	