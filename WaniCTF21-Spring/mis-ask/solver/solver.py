with open('ask.csv') as f:
    ask = [i.strip() for i in f.readlines()]

ask = ''.join(ask)

tmp = ''
for i in range(0, len(ask), 31):
    print(ask[i:i+31])
    tmp += ask[i]

tmp = hex(int(tmp, 2))
print(tmp)
