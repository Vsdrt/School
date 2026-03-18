from ipaddress import *

for x in range(33):
	net = ip_network(f"111.24.160.159/{x}", 0) 
	print(net, net.netmask)