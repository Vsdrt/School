from ipaddress import *


net = ip_network(f"192.168.31.80/255.255.255.240", 0)

mx = 0
for x in net:
	s = f"{x:b}"

	if s.count("1") > mx:
		mx = s.count("1")
	
print(mx)