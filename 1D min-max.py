import matplotlib.pyplot as plt
import numpy as np
import random
def fun(randomlist, m1, m2, iteration): #assigning clusters as per mean 
    C1 = []
    C2 = []
    iteration = iteration +1
    for i in range(0, len(randomlist)):
        a = abs(randomlist[i]-m1)
        b = abs(randomlist[i]-m2)
        if(a>=b):
            y = randomlist[i]
            C2.append(y)
        else:
            x = randomlist[i]
            C1.append(x)
    C2.sort()                   #sorts array
    C1.sort()                   #sorts array
    print("Min_Cluster:", C2)
    print("Max_Cluster:", C1)

randomlist = random.sample(range(0, 50), 45) #generates random list of array
print(randomlist)
m2 = min(randomlist)                #computes minimum point from an array
m1 = randomlist[1]-m2
for i in range(1,20):
    if((randomlist[i]-m2)>m1):
        m1=randomlist[i]            #gives maximum point from the minimum point
print("Min: M2= ", m2)
print("Max: M1= ", m1)
iteration = 0
fun(randomlist, m1, m2, iteration)
