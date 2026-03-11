from ipaddress import *

for x in range(33):
	net = ip_network(f"90.155.69.100/{x}", 0)
	print(net, net.netmask)