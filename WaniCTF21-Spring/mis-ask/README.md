# ASK 252pt Easy
# 問題文
Amplitude Shift Keying

# やったこと
zipファイルを展開すると，0/1のデータが出てきました．
問題文からこれは振幅変調の結果を表したものであると推測できました．

問題のデータを眺めていると，連続する0/1の数の最小が31個であることが分かりました．そこで，31データで1クロックとなっていると考え，
31データごとに区切りを入れてみました．

```python
with open('ask.csv') as f:
    ask = [i.strip() for i in f.readlines()]

ask = ''.join(ask)

tmp = ''
for i in range(0, len(ask), 31):
    print(ask[i:i+31])
```

```
$ python solver.py
...
0000000000000000000000000000000
0000000000000000000000000000000
0000000000000000000000000000000
0000000000000000000000000000000
1111111111111111111111111111111
0000000000000000000000000000000
1111111111111111111111111111111
0000000000000000000000000000000
0000000000000000000000000000000
0000000000000000000000000000000
1111111111111111111111111111111
1111111111111111111111111111111
1111111111111111111111111111111
...
```

綺麗に0/1を分けることができました．

各行先頭のデータだけを集めたのち，16進数で表示してみると
以下のようになりました．

```python
with open('ask.csv') as f:
    ask = [i.strip() for i in f.readlines()]

ask = ''.join(ask)

tmp = ''
for i in range(0, len(ask), 31):
    print(ask[i:i+31])
    tmp += ask[i]

tmp = hex(int(tmp, 2))
print(tmp)
```
```
$ python solver.py
...
0x2aaaaaaab951931051ded85b1ccc0b5acc1bdddb8b4d1ccb4c1b8b4c19998b5ad95e4c5b99df4000000000000aaaaaaaae5464c41477b616c73302d6b306f776e2d34732d306e2d3066662d6b6579316e677d0000000000002aaaaaaab951931051ded85b1ccc0b5acc1bdddb8b4d1ccb4c1b8b4c19998b5ad95e4c5b99df4000000000000aaaaaaaae5464c41477b616c73302d6b306f776e2d34732d306e2d3066662d6b6579316e677d0000000000002aaaaaaab951931051ded85b1ccc0b5acc1bdddb8b4d1ccb4c1b8b4c19998b5ad95e4c5b99df4000000000000aaaaaaaae5464c41477b616c73302d6b306f776e2d34732d306e2d3066662d6b6579316e677d0000000000002aaaaaaab951931051ded85b1ccc0b5acc1bdddb8b4d1ccb4c1b8b4c19998b5ad95e4c5b99df4000000000000aaaaaaaae5464c41477b616c73302d6b306f776e2d34732d306e2d3066662d6b6579316e677d0000000000002aaaaaaab951931051ded85b1ccc0b5acc1bdddb8b4d1ccb4c1b8b4c19998b5ad95e4c5b99df4000000000000aaaaaaaae5464c41477b616c73302d6b306f776e2d34732d306e2d3066662d6b6579316e677d
```

464c4147...の値が何度か繰り替えされているのが見えます．
これは文字列'FLAG'を16進法で表したものです．

```python
>>> [hex(ord(c)) for c in 'FLAG']
['0x46', '0x4c', '0x41', '0x47']
```

フラグっぽい部分を取り出して，文字列に直してみます．

```python
ask = '464c41477b616c73302d6b306f776e2d34732d306e2d3066662d6b6579316e677d'
flag = ''

for i in range(0, len(ask), 2):
    c = chr(int(ask[i:i+2], 16))
    flag += c

print(flag)
```

```
$ python solver2.py
FLAG{als0-k0own-4s-0n-0ff-key1ng}
``．
実行するとフラグが得られました．

# フラグ
FLAG{als0-k0own-4s-0n-0ff-key1ng}
