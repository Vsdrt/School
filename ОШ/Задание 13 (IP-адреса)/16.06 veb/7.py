from ipaddress import *

for x in range(33):
	net1 = ip_network(f"151.172.115.121/{x}", 0)
	net2 = ip_network(f"151.172.115.156/{x}", 0)

	if net1 != net2:
		print(x, "True", net1, net2)