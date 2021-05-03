target = []
target.append('7941081424088616006')
target.append('7311705455698409823')
target.append( '3560223458505028963')
target.append('35295634984951667')

print(target)

hs = []
for t in target:
    h = hex(int(t))[2:]
    print(h)
    hs.append(h)

for h in hs:
    print(f'### for {h} ###') 
    f = ''
    for i in range(0, len(h), 2):
        c = h[i:i+2]
        f += chr(int(c, 16))
    
    print(f[::-1])
