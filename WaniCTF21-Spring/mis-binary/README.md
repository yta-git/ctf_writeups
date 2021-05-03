# binary (156pt Beginner)
# 問題文
文字も所詮1と0の集合です。
sample.pyを参考に復号器を作ってみてください。

# やったこと

zipファイルを展開したら，0と1からなるbinary.csvと，サンプルスクリプトが出てきました．

```
0
1
0
0
0
1
1
0
0
...
```

```python
s = "WANI"
bits = []
for i in range(len(s)):
    val = s[i]
    for j in range(8):
        b = (ord(val) >> (7 - j)) & 0x01
        bits.append(b)

print(bits)

s = ""
c = 0
for i in range(len(bits)):
    val = int(bits[i])
    c = (c << 1) | val
    if i % 8 == 7:
        s = s + chr(c)
        c = 0

print(s)
```

サンプルスクリプトは文字列"WANI"を0/1に変換したのち，
0/1をもう一度文字列”WANI”に戻しているようです．

スクリプトの後半部分を利用して，binary.csvからフラグを取り出してみます．

```python
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

```

```
$ python solver.py 
FLAG{the_basic_knowledge_of_communication}
```
フラグが得られました．

# フラグ
FLAG{the_basic_knowledge_of_communication}

