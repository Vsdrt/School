from ipaddress import *

net = ip_network("192.168.32.160/255.255.255.240", 0)

k = 0
for x in net:
	s = '.'.join(f"{bin(int(c))[2:]:0>8}" for c in str(x).split("."))
	s = f"{x:b}"
	print(x, s)
	if s.count("1")%2==0:
		k += 1

print(k)