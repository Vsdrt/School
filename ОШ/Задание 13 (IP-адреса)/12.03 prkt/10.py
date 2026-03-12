from ipaddress import *

net = ip_network(f"45.172.106.203/255.255.252.0", 0)

print(max(net))