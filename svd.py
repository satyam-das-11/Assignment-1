import numpy as np
import time
A1=[[2,1],[1,0]]
A2=[[2,1],[1,0],[0,1]]
A3=[[2,1],[-1,1],[1,1],[2,-1]]
A4=[[1,1,0],[-1,0,1],[0,1,-1],[1,1,-1]]
A5=[[0,1,1],[0,1,0],[1,1,0],[1,0,1]]
A=[A1,A2,A3,A4,A5]
for i in range(len(A)):
    start=time.time()
    print("Matrix-%d :"%(i+1))
    print(A[i])
    U,S,V=np.linalg.svd(A[i])
    print("U matrix:")
    print(U)
    print("S matrix :")
    print(S)
    print("VT matrix :")
    print(V)
    end=time.time()
    D=(end-start)*10**3
    print("Run time :")
    print(D,"ms")
    print("------------------------------")
