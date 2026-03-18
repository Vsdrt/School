from ipaddress import *


for x in range(33):
	net = ip_network(f"192.75.64.98/{x}",0 )

	print(net, net.netmask)