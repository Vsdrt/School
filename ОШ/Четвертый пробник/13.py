from ipaddress import *


for x in range(33):
	net1 = ip_network(f"193.175.175.231/{x}", 0)
	net2 = ip_network(f"193.175.176.118/{x}", 0)

	if net1 != net2:
		print(net1.netmask)