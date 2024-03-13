from ipaddress import ip_network

k = 0
net = ip_network('131.72.131.45/255.255.255.192', False)
for ad in net:
    t = bin(int(ad))[2:].ljust(32, '0')
    if t.count('1') % 2 != 0:
        k += 1
print(k)