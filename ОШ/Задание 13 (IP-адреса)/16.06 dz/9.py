from ipaddress import *

net = ip_network("101.157.240.0/255.255.252.0", 0)
k = 0

for i in net:
	s = f"{i:b}"
	if s[:16].count("1") > s[16:].count("1"):
		k += 1

print(k)