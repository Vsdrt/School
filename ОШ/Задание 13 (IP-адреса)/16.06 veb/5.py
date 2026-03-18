from ipaddress import *

x = 26
net = ip_network(f"121.171.5.70/{x}", 0)
k = 0

for x in net:
	print(x)
	k += 1

print(k)