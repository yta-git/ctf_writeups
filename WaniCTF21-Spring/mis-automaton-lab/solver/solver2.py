from pwn import *
from solver import solve

with open('list') as f:
    ls = [i.replace('\n', '') for i in f.readlines()]

for i in ls:
    con = remote('automaton.mis.wanictf.org', 50020)

    con.recvuntil('(press enter key to continue)')
    con.send('\n')
    con.recvline()

    # 1
    print('### 1 ###')
    print(con.recvline())
    init = con.recvline().split()[-1].decode()
    gen  = int(con.recvline().split()[-1])
    print(init, gen)

    ans = solve(str(init), gen)
    print('ans:', ans)
    con.sendline(ans)

    # 2
    print('### 2 ###')
    print(con.recvline())
    init = con.recvline().split()[-1].decode()
    gen  = int(con.recvline().split()[-1])
    print(init, gen)

    ans = solve(init, gen)
    print('ans:', ans)
    con.sendline(ans)

    # 3
    print('### 3 ###')
    print(con.recvline())
    init = con.recvline().split()[-1].decode()
    gen  = int(con.recvline().split()[-1])

    print(init, gen)

    ans = i
    print('ans:', ans)
    con.sendline(ans)
    res = con.recvline().decode()
    print(res)
    if 'disappointed' in res:
        con.close()
        continue
    else:
        break

con.interactive()


