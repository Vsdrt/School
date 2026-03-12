from ipaddress import *


net = ip_network(f"98.81.154.195/255.252.0.0", 0)

print(max(net))