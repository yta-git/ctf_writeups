with open('binary.csv') as f:
    bits = [i[0] for i in f.readlines()]

s = ""
c = 0
for i in range(len(bits)):
    val = int(bits[i])
    c = (c << 1) | val
    if i % 8 == 7:
        s = s + chr(c)
        c = 0

print(s)
