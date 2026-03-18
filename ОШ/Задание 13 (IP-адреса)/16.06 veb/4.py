from ipaddress import *


net = ip_network("192.168.240.0/255.255.255.0", 0)
k = 0

for i in net:
	s = f"{i:b}"
	if s.count("0") == s.count("1"):
		k += 1

print(k)