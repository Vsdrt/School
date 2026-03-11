from ipaddress import *


for x in range(33):
	net = ip_network(f"251.211.38.240/{x}", 0)
	print(net, net.netmask)