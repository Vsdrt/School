from ipaddress import *


net = ip_network("115.192.0.0/255.192.0.0", 0)
k = 0

for x in net:
	s = f"{x:b}"
	if s.count("1") % 3 != 0:
		k += 1

print(k)