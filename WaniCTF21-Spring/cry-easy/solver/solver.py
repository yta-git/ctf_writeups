A = 5
B = 8

plaintext_space = "ABCDEFGHIJKLMNOPQRSTUVWXYZ_{}"

def encrypt(plaintext: str, a: int, b: int) -> str:
    ciphertext = ""
    for x in plaintext:
        if "A" <= x <= "Z":
            x = ord(x) - ord("A")
            x = (a * x + b) % 26
            x = chr(x + ord("A"))
        ciphertext += x

    return ciphertext

if __name__ == "__main__":

    target = 'HLIM{OCLSAQCZASPYFZASRILLCVMC}'
    flag = ''

    for i in range(len(target)):
        for c in plaintext_space:
            ciphertext = encrypt(c, a=A, b=B)
    
            if ciphertext == target[i]:
                flag += c
                print(flag)
                break
            
