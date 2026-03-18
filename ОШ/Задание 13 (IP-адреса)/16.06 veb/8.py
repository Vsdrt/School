from ipaddress import *

net = ip_network("192.168.32.160/255.255.255.240", 0)
k = 0

for i in net:
	s = "".join([f"{bin(int(x))[2:]:>08}" for x in str(i).split(".")])
	print(s)

	if s.count("0") > 21:
		k += 1

print(k)