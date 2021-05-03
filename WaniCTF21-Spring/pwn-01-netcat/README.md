# 01 netcat (142pt Beginner)
# 問題文

`nc netcat.pwn.wanictf.org 9001`
- netcat (nc)と呼ばれるコマンドを使うだけです。
- つないだら何も出力されなくても知っているコマンドを打ってみましょう。

## 使用ツール例
- netcat (nc)
- 
## gccのセキュリティ保護
- Full RELocation ReadOnly (RELRO)
- Stack Smash Protection (SSP)有効
- No eXecute bit(NX)有効
- Position Independent Executable (PIE)有効

# やったこと
指示どおりにコマンドを実行
```
$ nc netcat.pwn.wanictf.org 9001
congratulation!
please enter "ls" command
ls
chall
flag.txt
redir.sh
cat flag.txt
FLAG{this_is_the_same_netcat_problem_as_previous_one}
```
中にflag.txtの中身を見るとフラグがありました．

# フラグ
FLAG{this_is_the_same_netcat_problem_as_previous_one}

