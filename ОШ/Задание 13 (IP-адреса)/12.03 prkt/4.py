from ipaddress import *

net  = ip_network(f"87.226.26.72/255.255.255.252", 0)

k = 0
for x in net:
	s = f"{x:b}"
	if s.count("0")%2==0:
		k += 1
	
print(k)