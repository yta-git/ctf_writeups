ask = '464c41477b616c73302d6b306f776e2d34732d306e2d3066662d6b6579316e677d'
flag = ''

for i in range(0, len(ask), 2):
    c = chr(int(ask[i:i+2], 16))
    flag += c

print(flag)
    
