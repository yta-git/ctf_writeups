# execute (190pt Easy)
# 問題文

コマンドを間違えて、ソースコードも消しちゃった！

今残っているファイルだけで実行して頂けますか？

(reverse engineeringすれば、実行しなくても中身は分かるみたいです。)

# やったこと

zipファイルを展開すると，main.sなるアセンブリのファイルが出てきました．

```
...
main:
.LFB0:
	.cfi_startproc
	endbr64
	pushq	%rbp
	.cfi_def_cfa_offset 16
	.cfi_offset 6, -16
	movq	%rsp, %rbp
	.cfi_def_cfa_register 6
	subq	$48, %rsp
	movq	%fs:40, %rax
	movq	%rax, -8(%rbp)
	xorl	%eax, %eax
	movabsq	$7941081424088616006, %rax
	movabsq	$7311705455698409823, %rdx
	movq	%rax, -48(%rbp)
	movq	%rdx, -40(%rbp)
	movabsq	$3560223458505028963, %rax
	movabsq	$35295634984951667, %rdx
	movq	%rax, -32(%rbp)
	movq	%rdx, -24(%rbp)
	leaq	-48(%rbp), %rax
	movq	%rax, %rdi
	call	print@PLT
	movl	$0, %eax
	movq	-8(%rbp), %rcx
	xorq	%fs:40, %rcx
	je	.L3
	call	__stack_chk_fail@PLT
...
```

即値
- $7941081424088616006
- $7311705455698409823
- $3560223458505028963
- $35295634984951667

が目立って見えます．

文字列に変換してみます．

```python
target = []
target.append('7941081424088616006')
target.append('7311705455698409823')
target.append( '3560223458505028963')
target.append('35295634984951667')

print(target)

hs = []
for t in target:
    h = hex(int(t))[2:]
    print(h)
    hs.append(h)

for h in hs:
    print(f'### for {h} ###') 
    f = ''
    for i in range(0, len(h), 2):
        c = h[i:i+2]
        f += chr(int(c, 16))
    
    print(f[::-1])
```

```
$ python solver.py       
['7941081424088616006', '7311705455698409823', '3560223458505028963', '35295634984951667']
6e34637b47414c46
6578655f7530795f
3168745f65347563
7d653169665f73
### for 6e34637b47414c46 ###
FLAG{c4n
### for 6578655f7530795f ###
_y0u_exe
### for 3168745f65347563 ###
cu4e_th1
### for 7d653169665f73 ###
s_fi1e}
```

出力された文字列を結合したものがフラグでした．

# フラグ
FLAG{c4n_y0u_execu4e_th1s_fi1e}