from ipaddress import *


for x in range(33):
	net = ip_network(f"130.140.241.137/{x}", 0)
	print(net, net.netmask)