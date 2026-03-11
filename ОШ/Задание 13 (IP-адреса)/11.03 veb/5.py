from ipaddress import *


net  = ip_network(f"158.132.161.128/255.255.255.128", 0)

k = 0
for x in net: 
	if bin(int(str(x)[-3:]))[2:][-1] == "1":
		#print(x, bin(int(str(x)[-3:]))[2:])
		k += 1
	
print(k)