with open('manchester.csv') as f:
    ask = [i.strip() for i in f.readlines()]

ask = ''.join(ask)

tmp = ''
for i in range(0, len(ask), 31):
    print(ask[i:i+31])
    tmp += ask[i]

print(tmp)

tmp2 = ''
for i in range(0, len(tmp), 2):
    
    bit = tmp[i:i+2]
    print(bit)

    if bit == '01':
        tmp2 += '0'
    else:
        tmp2 += '1'

print(tmp2)

tmp2 = hex(int(tmp2, 2))
print(tmp2)
