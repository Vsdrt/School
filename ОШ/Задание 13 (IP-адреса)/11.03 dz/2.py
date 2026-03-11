from ipaddress import *

for x in range(33):
	net = ip_network(f"190.120.251.78/{x}", 0)
	print(net, net.netmask)