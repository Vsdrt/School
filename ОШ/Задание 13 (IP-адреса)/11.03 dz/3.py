from ipaddress import *

for x in range(33):
	net = ip_network(f"134.73.209.97/{x}", 0)
	print(net, net.netmask)