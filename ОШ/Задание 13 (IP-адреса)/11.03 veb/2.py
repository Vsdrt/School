from ipaddress import *

for x in range(33):
	net = ip_network(f"229.117.114.172/{x}", 0)
	print(net, net.netmask)
		


