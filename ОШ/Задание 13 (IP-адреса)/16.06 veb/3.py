from ipaddress import *



for x in range(33):
	net = ip_network(f"133.57.64.130/{x}", 0)
	print(net, net.netmask)