from ipaddress import *

net = ip_network("235.86.56.0/255.255.248.0", 0)
k = 0

for i in net:
	s = "".join([f"{bin(int(x))[2:]:>08}" for x in str(i).split(".")])
	if s[-2:] == "11":
		k +=1

print(k)