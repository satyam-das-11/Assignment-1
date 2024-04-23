#value of pi(direct sampling Monte-carlo)
import matplotlib.pyplot as plt
import numpy as np
import random as r
Pi=[]
for j in range(1,100):
    N=1000*j #no. of sample points
    n=0
    xi,yi=[],[]
    xo,yo=[],[]
    for i in range(N):
        x=r.uniform(-1,1)
        y=r.uniform(-1,1)
        if (x**2 + y**2 <=1):
            n=n+1
            xi.append(x)
            yi.append(y)
        else:
            xo.append(x)
            yo.append(y)
    pi=(n*4/N)
    Pi.append(pi)
print(Pi)
'''plt.plot(xi,yi,'+') 
plt.plot(xo,yo,'.')
plt.title("Value of Pi : %f"%pi)'''
plt.hist(Pi,50)
plt.grid() 
plt.show()  
  