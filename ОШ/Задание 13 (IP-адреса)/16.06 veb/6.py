from ipaddress import *

for x in range(33):
	net1 = ip_network(f"167.77.194.37/{x}", 0)
	net2 = ip_network(f"167.77.194.47/{x}", 0)
	net3 = ip_network(f"167.77.200.25/{x}", 0)

	if net3 != net2 and net1 == net2:
		print(x, "True", net1, net2)