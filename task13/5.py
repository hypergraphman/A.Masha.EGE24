from ipaddress import ip_network

k = 0
net = ip_network('10.7.46.6/255.255.240.0', False)
for ad in net:
    t = bin(int(ad))[2:].ljust(32, '0')
    if t[16:].count('1') > 4:
        k += 1
print(k)