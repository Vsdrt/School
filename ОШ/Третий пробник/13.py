from ipaddress import ip_network


for x in range(33):
    net1 = ip_network(f"165.112.200.70/{x}", 0)
    net2 = ip_network(f"165.112.175.80/{x}", 0)
    if net1 == net2:
        print(x)