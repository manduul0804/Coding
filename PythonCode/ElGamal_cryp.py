p = 29
g = 2
x = 5

def public_key(p1,g1,x1):
    g_mod = (g1**x1) % p1
    print(f"Public key: {p1}, {g1}, {g_mod}")
    print(f"Private key: {x1}")
    return g_mod

def encrypt(p1,g_mod1,M1):
    y =14
    # k = g^y mod p
    k = (g_mod1**y) % p1
    
    # d = M(g^x)^y mod p
    d=M1*(g_mod1**y) % p1

    print(f"C = ({k}, {d})")

def decrypt(p1,x1,k1,d1):
    # M = d * k^ p-1-x mod p
    M = d1 * (k1**(p1-1-x1)) % p1
    print(f"M = ({M})")

g_key = public_key(p,g,x)

m_num = 6
encrypt(p,g_key,m_num)
decrypt(p,6,21,11)