from ipaddress import *



for x in range(33):
	net1 = ip_network(f"112.117.107.70/{x}", 0)
	net2 = ip_network(f"112.117.121.80/{x}", 0)
	if net1 == net2:
		print(net1.num_addresses)