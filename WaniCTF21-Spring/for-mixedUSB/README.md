# MixedUSB (175pt Very hard)
# 問題文
USBにパーティションを設定したら、どこにFLAGを保存しているのかわからなくなってしまいました．．．

# やったこと
MixedUSB.imgというファイルが与えられました．
おもむろにstringsコマンドを使って文字列を抽出してみました．

```
$ strings MixedUSB.img
...
DUMMY{baz}
DUMMY{foo}
DUMMY{qux}
DUMMY{baz}
DUMMY{quux}
FLAG{mixed_file_allocation_table}
```

フラグが出てきました．

# フラグ
FLAG{mixed_file_allocation_table}

