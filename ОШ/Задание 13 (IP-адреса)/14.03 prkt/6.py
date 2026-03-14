from ipaddress import *


net = ip_network("102.162.200.51/255.255.255.0", 0)
mx = max(net)
print(mx)
print(102 + 162 + 200 + 254)