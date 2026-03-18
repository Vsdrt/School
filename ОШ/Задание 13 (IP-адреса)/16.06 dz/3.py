from ipaddress import *

for x in range(33):
	net = ip_network(f"158.116.11.146/{x}", 0)
	print(net)