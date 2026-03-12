from ipaddress import *

net = ip_network(f"214.96.0.0/255.240.0.0", 0)

k = 0
for x in net:
	s = f"{x:b}"
	if s.count("0")%3==0:
		k += 1

print(k)