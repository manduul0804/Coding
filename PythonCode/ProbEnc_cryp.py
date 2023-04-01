

def randBits(x1,n1):
    xAns = (x1 ** 2) % n1
    return xAns
 

x0 = 3530
n =8137
p = 79
M = [0,0,1,0,0,0,1,1]

B = []
C = []
temp = x0

for i in range(len(M)):
    
    bitNum=randBits(temp, n)
    if ((bitNum % 2) == 0):
        B.append(0)
    else:
        B.append(1)
    temp = bitNum
    print(f"X{i} = {temp}")

print(B)

sumMandC =[]

for i in range(len(M)):
    sumMandC.append(M[i] + B[i])



for i in sumMandC:
    if(i == 2 or i == 0):
        C.append(0)
    else:
        C.append(1)

print(f"C = {C}")