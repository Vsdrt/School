from ipaddress import *

net = ip_network("151.192.0.0/255.224.0.0", 0)
k = 0


for i in net:
	#s = f"{i:b}"
	s = "".join([f'{bin(int(x))[2:]:>08}' for x in str(i).split(".")])
	if s.count("1") == s.count("0"):
		k += 1

print(k)