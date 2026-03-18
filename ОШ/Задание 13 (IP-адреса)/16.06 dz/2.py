from ipaddress import *

for x in range(33):
	
	net = ip_network(f"168.224.22.193/{x}", 0)
	print(net)