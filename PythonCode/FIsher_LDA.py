import numpy as np

mx1 = np.array([[1,2], [2,3],[3,3],[4,5],[5,5]])
mx2 = np.array([[1,0], [2,1],[3,1],[3,2],[5,3],[6,5]])
m_mean1 = np.mean(mx1, axis=0, keepdims = True)
m_mean2 = np.mean(mx2, axis=0, keepdims = True)
print(mx1)
print("\nMatrix mean 1")
print(m_mean1)
print("\nMatrix mean 2")
print(m_mean2)



mean_corrected1 = np.subtract(mx1,m_mean1)
print("\nMean corrected value 1")
print(mean_corrected1)

mean_corrected2 = np.subtract(mx2,m_mean2,)
print("\nMean corrected value 2")
print(mean_corrected2)

print("\nmean2 - mean1")
mean_sub = np.subtract(m_mean2, m_mean1)
print(mean_sub)

S_B = mean_sub.T.dot(mean_sub)
print("\nS_B value is ")
print(S_B)

SC1 = mean_corrected1.T.dot(mean_corrected1)
print("\nSC1 value is")
print(SC1)

SC2 = mean_corrected2.T.dot(mean_corrected2)
print("\nSC2 value is")
print(SC2)

SW = np.add(SC1,SC2)
print("\nSW value is")
print(SW)


SW_inver = np.linalg.inv(SW)

print("\nSW inverse")
print(SW_inver)

S_B_W = np.subtract(S_B, SW_inver)
print("\nS_inv * S_B")
print(S_B_W)

#Use wolfram and enter new values
S_B_W_new = np.array([[0.2622,-1.28551],[-0.29409,1.44017]])
print("\nEigenvalues")
w,v = np.linalg.eig(S_B_W_new)
print("\nLargest eigenvalue. Take the largest")
print(w)
print("\nNormalized eigenvector. Take corresbonding column")
print(v)

m_norm = np.array([[0.9278,0.373]])
print("\nclass1")
print(np.multiply(m_norm,m_mean1.T))