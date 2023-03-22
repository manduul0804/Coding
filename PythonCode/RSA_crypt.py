
e = 11
p = 19
q = 13
n = p * q

def findD(p1, q1, e1):
    n1 = p1 * q1
    print(f"n = {n1}")
    n2 = (p1-1)*(q1-1)
    print(f"n2 = {n2}")
    
    #finding inverse mod
    for X in range(1, n2):
        if (((e1 % n2) * (X % n2)) % n2 == 1):
            return X
    return -1

def decrypt(C1, d1, n1):
    M = (C1 ** d1) % n1
    print(f"M = {M}")

def cipher(M1, e1, n1):
    C = (M1 ** e1) % n1
    print(f"C = {C}")


inMod = findD(p,q,e)
print(f"d = {inMod}")
decrypt(63,121,247)
