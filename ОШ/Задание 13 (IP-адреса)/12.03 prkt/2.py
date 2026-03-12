from ipaddress import *

for x in range(33):
	net = ip_network(f"163.232.136.60/{x}", 0)
	print(net, net.netmask)