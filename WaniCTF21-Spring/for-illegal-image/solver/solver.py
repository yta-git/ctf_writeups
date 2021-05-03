from scapy.all import *

p = rdpcap('illegal_image.pcap').filter(lambda p:Raw in p and ICMP in p and p['IP'].src == '192.168.0.158')

data = b''
for i in range(len(p)):

    load = p[i]['Raw'].load
    data += load

print(data)

with open('data.jpg', 'wb') as f:
    f.write(data)
    f.close()