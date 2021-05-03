with open('output.txt') as f:
    cipher = int(f.read().replace('\n', ''))

print(cipher)

cipher_hex = str(hex(cipher))[2:]
print(cipher_hex)

flag = ''
for i in range(0, len(cipher_hex), 2):
    flag += chr(int(cipher_hex[i:i+2], 16))

print(flag)