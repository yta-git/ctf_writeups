def next(state):
    state = state[-1] + state + state[0]
    res = ''

    for i in range(1, 16):
        tmp = state[i-1:i+2]
        
        if tmp in ('111', '110', '101', '000'):
            res += '0'

        else:
            res += '1'

    return res


def solve(init, gen):

    # states = set()
    # states.add(init)

    for i in range(gen):
        init = next(init)
        # print(i, init)
        # states.add(init)
#        print(len(states))

#    for i in states:
#        print(i)

    return init

if __name__ == '__main__':
    for i in range(3):
        init, gen = input().split()
        res = solve(init, int(gen))
        print('ans:', res)

# 1 ... ok
# 2 ... ok
# 3 ... ? -> only 1052 pattern