from ipaddress import *

net = ip_network("185.8.0.0/255.255.128.0", 0)
mx = 0


for i in net:
	s = f"{i:b}"
	if s.count("1") > mx:
		mx = s.count("1")

print(mx)