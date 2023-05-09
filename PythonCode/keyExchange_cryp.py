

p = 89
g = 6
a = 18
b = 33

def encrypt(p1,g1,a1):
    # A=g^a mod p
    A = (g1**a1) % p1
    print(f"A = {A}")
    return A

def decrypt(p1,g1,b1):
    # B = g^b mod p
    B = (g1**b1) % p1
    print(f"B = {B}")
    return B


def comKey(B1,a1, p1):
    # K_A = B^a mod p1
    K = (B1**a1) % p1
    print(f"Common key = {K}")

A = encrypt(p,g,a)
B = decrypt(p,g,b)


print("Printing common key")

comKey(B,a,p)
comKey(A,b,p)
# print("Printing B value")
# decrypt(p,g,B)

