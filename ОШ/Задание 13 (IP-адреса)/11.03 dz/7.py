from ipaddress import * 

net = ip_network(f"135.221.128.0/255.255.128.0", 0)

mn = 10**10
for x in net:
	s = f"{x:b}"
	if s.count("1") < mn:
		mn = s.count("1")

print(mn)