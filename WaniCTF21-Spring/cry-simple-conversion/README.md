# Simple conversion (154pt Beginner)
# 問題文
戻し方を忘れました…

# やったこと

もらったzipファイルを展開するとPythonスクリプトと実行結果が出てきました．

```py
from const import flag

def bytes_to_integer(x: bytes) -> int:
    x = int.from_bytes(x, byteorder="big")
    return x

print(bytes_to_integer(flag))

```

``` 
709088550902439876921359662969011490817828244100611994507393920171782905026859712405088781429996152122943882490614543229
```

フラグ文字列のバイト値をint型に変換して出力している様です．

int型の値を16進数に変換したのち，文字列に変換するスクリプトを書けば良さそうです．
以下のスクリプトを書きました．

```py
with open('output.txt') as f:
    cipher = int(f.read().replace('\n', ''))

print(cipher)

cipher_hex = str(hex(cipher))[2:]
print(cipher_hex)

flag = ''
for i in range(0, len(cipher_hex), 2):
    flag += chr(int(cipher_hex[i:i+2], 16))

print(flag)
```

実行したらフラグが復号できました．
```
709088550902439876921359662969011490817828244100611994507393920171782905026859712405088781429996152122943882490614543229
464c41477b376831735f69355f6830775f77655f63306e766572745f6d337373406765735f316e74305f6e756d363372737d
FLAG{7h1s_i5_h0w_we_c0nvert_m3ss@ges_1nt0_num63rs}
```

# フラグ
FLAG{7h1s_i5_h0w_we_c0nvert_m3ss@ges_1nt0_num63rs}

# メモ

公式writeupみたら
```
flag.to_bytes((flag.bit_length() + 7 // 8), byteorder='big')
```
で変換してた．そういう関数があるのね．
