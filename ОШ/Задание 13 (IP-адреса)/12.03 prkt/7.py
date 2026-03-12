from ipaddress import *


for x in range(33):
	net = ip_network(f"151.168.147.193/{x}", 0)
	print(net, net.netmask)