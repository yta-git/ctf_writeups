# Manchester (269pt Normal)
# 問題文
Manchester Encoding

# やったこと

zipファイルを展開すると0/1のデータが得られました．
また，問題文からマンチェスタ符号を復号するとフラグが得られると考えました．

31データで1クロックであると考え，データを復調してみます．
```python
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
```

```
$ python solver.py
...
0x1ffffffffffc464c41477b61766f6964696e672d636f6e736563746976652d6f6e65732d616e642d7a65726f737dffffffffffe232620a3bdb0bb37b4b234b73396b1b7b739b2b1ba34bb3296b7b732b996b0b73216bd32b937b9befffffffffff11931051ded85d9bda591a5b99cb58dbdb9cd958dd1a5d994b5bdb995ccb585b990b5e995c9bdcdf7ffffffffff88c98828ef6c2ecded2c8d2dcce5ac6dedce6cac6e8d2ecca5adedccae65ac2dcc85af4cae4dee6fbffffffffffc464c41477b61766f6964696e672d636f6e736563746976652d6f6e65732d616e642d7a65726f737d
```
464c4147...の値が何度か繰り替えされているのが見えます．
これは文字列'FLAG'を16進法で表したものです．

```python
>>> [hex(ord(c)) for c in 'FLAG']
['0x46', '0x4c', '0x41', '0x47']
```

フラグっぽい部分を取り出して，文字列に直してみます．

```python
man = '464c41477b61766f6964696e672d636f6e736563746976652d6f6e65732d616e642d7a65726f737d'
flag = ''

for i in range(0, len(ask), 2):
    c = chr(int(ask[i:i+2], 16))
    flag += c

print(flag)
```

```
$ python solver2.py 
FLAG{avoiding-consective-ones-and-zeros}
```

フラグが得られました．

# フラグ
FLAG{avoiding-consective-ones-and-zeros}