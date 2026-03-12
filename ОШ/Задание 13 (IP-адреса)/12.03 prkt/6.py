from ipaddress import *


for x in range(33):
	net = ip_network(f"92.52.42.52/{x}", 0)
	print(net, net.netmask)