#Binomial convolution
import numpy as np
M=[0.215,0.785]  #1st trial
N=4
p=np.pi/4 # probability of hitting
for i in range(len(M)-1,N):
    #M[0]=(1-p)*M[0]
    M_k_1=p*M[i]
    for k in range(1,len(M)):
        M[k]=p*M[k-1]+(1-p)*M[k]
    M[0]=(1-p)*M[0]
    #M_k_1=p*M[i]
    M.append(M_k_1)
    print("%d th trial" %(i+1))
    print(M)
    
    
    