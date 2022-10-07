import ipaddress

ip = '192.168.0.0/4'

# addr = ipaddress.ip_address(ip)
# print(addr + 100)

net = ipaddress.ip_network(ip, strict=False)

for ip in net:
    print(ip)