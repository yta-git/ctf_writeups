# Easy (166pt Easy)
# 問題文
手始めに

# やったこと

もらったzipファイルを展開するとPythonスクリプトと実行結果が出来てきました．

```py
with open("flag.txt") as f:
    flag = f.read().strip()


A = REDACTED
B = REDACTED

plaintext_space = "ABCDEFGHIJKLMNOPQRSTUVWXYZ_{}"

assert all(x in plaintext_space for x in flag)


def encrypt(plaintext: str, a: int, b: int) -> str:
    ciphertext = ""
    for x in plaintext:
        if "A" <= x <= "Z":
            x = ord(x) - ord("A")
            x = (a * x + b) % 26
            x = chr(x + ord("A"))
        ciphertext += x

    return ciphertext


if __name__ == "__main__":
    ciphertext = encrypt(flag, a=A, b=B)
    print(ciphertext)
```

```
HLIM{OCLSAQCZASPYFZASRILLCVMC}
```

暗号化は一文字づつ行われているようです．
また，復号するにはAとBの値が必要です．

初めにAとBの値を推測することから始めました．
フラグの形式は`FLAG{}`なので,
`FLAG`を暗号化したときに出力が`HLIM`になるようなパラメータA, Bを探します．

提供されたスクリプトを見ると，A, Bは0~25のどれかだと推測できます．
```py
            x = (a * x + b) % 26
```

encrypt.pyを改造したスクリプトを用意して，
総当たりで探索してみます．

```py
...
    for A in range(26):
        for B in range(26):
            flag = 'FLAG'
            ciphertext = encrypt(flag, a=A, b=B)

            if ciphertext == 'HLIM':
                print(ciphertext, A, B)
...
```
```
$ python encrypt.py 
HLIM 5 8             
```

これでA=5, B=8とわかりました．

フラグと暗号文は一文字づつそれぞれ対応しているため，
得られたA,Bをつかって
一文字づつ総当たりでFLAGを探していきます．

```py
A = 5
B = 8

plaintext_space = "ABCDEFGHIJKLMNOPQRSTUVWXYZ_{}"

def encrypt(plaintext: str, a: int, b: int) -> str:
    ciphertext = ""
    for x in plaintext:
        if "A" <= x <= "Z":
            x = ord(x) - ord("A")
            x = (a * x + b) % 26
            x = chr(x + ord("A"))
        ciphertext += x

    return ciphertext

if __name__ == "__main__":

    target = 'HLIM{OCLSAQCZASPYFZASRILLCVMC}'
    flag = ''

    for i in range(len(target)):
        for c in plaintext_space:
            ciphertext = encrypt(c, a=A, b=B)
    
            if ciphertext == target[i]:
                flag += c
                print(flag)
                break
```

```
$ python solver.py 
F
FL
FLA
FLAG
FLAG{
FLAG{W
FLAG{WE
FLAG{WEL
FLAG{WELC
FLAG{WELCO
FLAG{WELCOM
FLAG{WELCOME
FLAG{WELCOMET
FLAG{WELCOMETO
FLAG{WELCOMETOC
FLAG{WELCOMETOCR
FLAG{WELCOMETOCRY
FLAG{WELCOMETOCRYP
FLAG{WELCOMETOCRYPT
FLAG{WELCOMETOCRYPTO
FLAG{WELCOMETOCRYPTOC
FLAG{WELCOMETOCRYPTOCH
FLAG{WELCOMETOCRYPTOCHA
FLAG{WELCOMETOCRYPTOCHAL
FLAG{WELCOMETOCRYPTOCHALL
FLAG{WELCOMETOCRYPTOCHALLE
FLAG{WELCOMETOCRYPTOCHALLEN
FLAG{WELCOMETOCRYPTOCHALLENG
FLAG{WELCOMETOCRYPTOCHALLENGE
FLAG{WELCOMETOCRYPTOCHALLENGE}
```
フラグの復号ができました．

# フラグ
FLAG{WELCOMETOCRYPTOCHALLENGE}
