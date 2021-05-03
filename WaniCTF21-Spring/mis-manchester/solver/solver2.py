ask = '464c41477b61766f6964696e672d636f6e736563746976652d6f6e65732d616e642d7a65726f737d'
flag = ''

for i in range(0, len(ask), 2):
    c = chr(int(ask[i:i+2], 16))
    flag += c

print(flag)
    
