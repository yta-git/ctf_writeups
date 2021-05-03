# timer (202pt Hard)
# 問題文
フラグが出てくるまで待てますか？

super_complex_flag_print_function 関数でフラグを表示しているようですが、難読化されているため静的解析でフラグを特定するのは難しそうです...

GDBを使って動的解析してみるのはいかがでしょうか？

# やったこと

zipファイルを展開すると実行ファイルtimerが出てきました．
```
$ ./timer 

  ████████╗██╗███╗   ███╗███████╗██████╗ 
  ╚══██╔══╝██║████╗ ████║██╔════╝██╔══██╗
     ██║   ██║██╔████╔██║█████╗  ██████╔╝
     ██║   ██║██║╚██╔╝██║██╔══╝  ██╔══██╗
     ██║   ██║██║ ╚═╝ ██║███████╗██║  ██║
     ╚═╝   ╚═╝╚═╝     ╚═╝╚══════╝╚═╝  ╚═╝

I'll show the flag when the timer is 0 seconds.

259200 seconds left.
259199 seconds left.
259198 seconds left.
```
待つだけでフラグがもらえるが待っていられないので
指示どおりgdbで開いてみる．

```
$ gdb timer
...
gdb-peda$ start
```

問題文より，super_complex_flag_print_functionを実行すれば良いっぽいため，
jumpコマンドを使って制御をそちらに飛ばしてみる

```
gdb-peda$ jump super_complex_flag_print_function 
Continuing at 0x555555555174.
The time has come. Flag is "FLAG{S0rry_Hav3_you_b3en_wai7ing_lon6?_No_I_ju5t_g0t_her3}"
[Inferior 1 (process 359442) exited normally]
Warning: not running
```
フラグが表示された．


# フラグ
FLAG{S0rry_Hav3_you_b3en_wai7ing_lon6?_No_I_ju5t_g0t_her3}