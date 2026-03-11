from ipaddress import *

for x in range(33):
	net = ip_network(f"215.181.200.27/{x}", 0)
	print(net, net.netmask)