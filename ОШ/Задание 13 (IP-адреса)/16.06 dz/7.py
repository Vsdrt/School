from ipaddress import *

net = ip_network("180.23.32.0/255.255.240.0", 0)
k = 0

for i in net:
	s = "".join([f"{bin(int(x))[2:]:>08}" for x in str(i).split(".")]) 
	s = f"{i:b}"
	if s.count("1")%2==0:
		k += 1

print(k) 