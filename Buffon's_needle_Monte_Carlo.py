#Buffon's needle experiment to find value of pi

import random as r
import numpy as np
import matplotlib.pyplot as plt
n=1000000 # no. of trials
b=4.0 # distance between two cracks
a=3.0 # length of needle

#direct-needle----------------------------------------
N_hits=0 # no. of hits on a crack
for i in range(n):
    x_center=r.uniform(0,b/2)
    phi=r.uniform(0,np.pi/2)
    x_tip=x_center - (a/2)*np.cos(phi)
    if (x_tip<0):
        N_hits=N_hits+1
print("value of pi(Direct-needle) : ")
print((2*a/b)*float(n)/N_hits)  

#direc-needle patch -----------------------------------
N_hits_p=0 # no. of hits on a crack
m=0
cos=[]
for i in range(n):
       x_center_p=r.uniform(0,b/2)
       d_x=r.uniform(0,1)
       d_y=r.uniform(0,1)
       D=np.sqrt(d_x**2 + d_y**2)
       if(D<=1):
           m=m+1
           x_tip_p=x_center_p - (a/2)*d_x/D
           cos.append(d_x/D)
           if (x_tip_p<0):
               N_hits_p=N_hits_p+1
print("value of pi(Direct-needle-patch) :")
print((2*a/b)*float(m)/N_hits_p)
plt.hist(cos,100)
plt.show()
