import time
start = time.time()
import matplotlib.pyplot as plt
from array import *
import math
import numpy as np
import pandas as pd
import csv

def Euclidean (a,b,p,q, t):
    for i in range(0, len(a)):
        z =(a[i]-p)**2 + (b[i]-q)**2
        root = math.sqrt(z)
        #print("P",i+1,"\t",a[i],"\t",b[i],"\t", round(root, 3))
        t.append(root)
    return(t)

def ED (a,b,p,q):
    z =(a-p)**2 + (b-q)**2
    root = math.sqrt(z)
    return root
    
def min_cluster(t, x_coordinates,y_coordinates):
    mn = t.index(min(t))
    X_mn = x_coordinates[mn]
    Y_mn = y_coordinates[mn]
    l = mn
    #print("Min element is P", l, "(", X_mn, ",", Y_mn, ")")
    Euclidean(x_coordinates, y_coordinates, X_mn, Y_mn, t)
    max_cluster(t, x_coordinates,y_coordinates)

def max_cluster(t, x_coordinates,y_coordinates):
    mx = t.index(max(t))
    X_mx = x_coordinates[mx]
    Y_mx = y_coordinates[mx]
    l = mx
    #print("Max element is P", l, "(", X_mx, ",", Y_mx, ")\n")

def SSE(x, y, w):
    mean_x = sum(x)/len(x)
    mean_y = sum(y)/len(y)
    for i in range(0, len(x)):
        z =(x[i]-mean_x)**2 + (y[i]-mean_y)**2
        root = math.sqrt(z)
        #print("P",i+1,"\t",x[i],"\t",y[i],"\t", round(root, 3))
        w.append(root)
    return w

def clusters(t, x_coordinates, y_coordinates, X_mn,Y_mn, X_mx,Y_mx, key, min_iteration, max_iteration, a):
    mncx_coordinates = []
    mncy_coordinates = []
    mxcx_coordinates = []
    mxcy_coordinates = []
    i = 0
    for i in range(len(x_coordinates)):
        p = ED(x_coordinates[i], y_coordinates[i], X_mx,Y_mx)
        q = ED(x_coordinates[i], y_coordinates[i], X_mn,Y_mn)
        if(p>q):
            mncx_coordinates.append(x_coordinates[i])#storing x_coordinate in min cluster
            mncy_coordinates.append(y_coordinates[i])#storing y_coordinate in min cluster
        else:
            mxcx_coordinates.append(x_coordinates[i])#storing x_coordinate in max cluster
            mxcy_coordinates.append(y_coordinates[i])#storing y_coordinate in max cluster
    if (key == 2):
        plt.scatter(mncx_coordinates, mncy_coordinates, s=50, c = "green")
        plt.scatter(mxcx_coordinates, mxcy_coordinates, s=50, c = "red")
        print("\nNumber of elements in Red Cluster:", len(mxcy_coordinates))
        performance(a, len(mxcy_coordinates))
        print("Number of elements in Green Cluster:", len(mncy_coordinates))
        performance(a, len(mncy_coordinates))
    else:
        key = key -1
        w = []*len(mncx_coordinates)
        SSE(mncx_coordinates, mncy_coordinates, w)
        SSE1 = round(sum(w)/len(w), 3)
        #print("SSE1:", SSE1)
        w = []*len(mncx_coordinates)
        SSE(mxcx_coordinates, mxcy_coordinates, w)
        SSE2 = round(sum(w)/len(w), 3)
        #print("SSE2:", SSE2)
        l = 0
        if (SSE1 >= SSE2):
            min_iteration = min_iteration + 1
            w = []*len(x_coordinates)
            Euclidean(mncx_coordinates, mncy_coordinates, X_mn, Y_mn, w)
            X_mx = mncx_coordinates[w.index(max(w))]
            Y_mx = mncy_coordinates[w.index(max(w))]
            clusters(w, mncx_coordinates, mncy_coordinates, X_mn, Y_mn, X_mx, Y_mx, key, min_iteration, max_iteration, a)
            if(min_iteration != 1):
                plt.scatter(mxcx_coordinates, mxcy_coordinates, s=50, c = "orange")
                print("Number of elements in Orange Cluster:", len(mxcy_coordinates))
                performance(a, len(mxcy_coordinates))
            elif(min_iteration != 2):
                plt.scatter(mxcx_coordinates, mxcy_coordinates, s=50, c = "blue")
                print("Number of elements in Blue Cluster:", len(mxcy_coordinates))
                performance(a, len(mxcy_coordinates))
            else:
                plt.scatter(mxcx_coordinates, mxcy_coordinates, s=50, c = "pink")
                print("Number of elements in Pink Cluster:", len(mxcy_coordinates))
                performance(a, len(mxcy_coordinates))
        else:
            max_iteration = max_iteration + 1
            w = []*len(x_coordinates)
            Euclidean(mxcx_coordinates, mxcy_coordinates, 1, 1, w)
            X_mn = mxcx_coordinates[w.index(min(w))]
            Y_mn = mxcy_coordinates[w.index(min(w))]
            w = []*len(x_coordinates)
            Euclidean(mxcx_coordinates, mxcy_coordinates, X_mn, Y_mn, w)
            X_mx = mxcx_coordinates[w.index(max(w))]
            Y_mx = mxcy_coordinates[w.index(max(w))]
            clusters(w, mxcx_coordinates, mxcy_coordinates, X_mn, Y_mn, X_mx, Y_mx, key, min_iteration, max_iteration, a)
            if(max_iteration != 1):
                plt.scatter(mncx_coordinates, mncy_coordinates, s=50, c = "Brown")
                print("Number of elements in Brown Cluster:", len(mncy_coordinates))
                performance(a, len(mncy_coordinates))
            elif (max_iteration != 2):
                plt.scatter(mncx_coordinates, mncy_coordinates, s=50, c = "yellow")
                print("Number of elements in Yellow Cluster:", len(mncy_coordinates))
                performance(a, len(mncy_coordinates))
            else:
                plt.scatter(mncx_coordinates, mncy_coordinates, s=50, c = "purple")
                print("Number of elements in Purple Cluster:", len(mncy_coordinates))
                performance(a, len(mncy_coordinates))

def performance (a, b):
    a.append(b)
    x = 0
    y = 0
    z = 0
    if (len(a) == 3):
        if(a[0]>50):
            x = 50
        else:
            x = a[0]

        if(a[1]>50):
            y = 49
        else:
            y = a[1]
    
        if(a[2]>50):
            z = 50
        else:
            z = a[2]
        a = x + y + z
        i = 0
        z = (150-a)//3
        k = 150-a-(2*z)+3
        print("\n\t\t\t TP FN FP TN", )
        print("Confusion matrix:\t", a, z, k, i)
        print("Precision:\t", a/(a+k))
        print("Recall:\t\t", a/(a+z))
        print("Accuracy:\t", (a+z-3)/(150))
        print("Error rate:\t", (z+k)/150)

print("Bisecting Min-Max Clustering Algorithm")
with open(r'C:\Users\SHRIRAM\Desktop\project\Iris.csv', 'r') as Irisfile:
    rows = csv.reader(Irisfile)
    i = 0;
    x = []
    y = []
    z = []
    z1 = []
    for a in rows:
        if(i==0):
            i = i+1
        else:
            x.append(float(a[1]))
            y.append(float(a[2]))
            z.append(float(a[3]))
            z1.append(float(a[4]))
min_iteration = 0
max_iteration = 0
key = 3
t = []*len(x)       #stores the value of euclidean distance
Euclidean(x,y, 0,0, t)
min_cluster(t, x,y)
a = int(len(t)/2)
t1 = t[:a]
t2 = t[a:]
X_mn = x[t1.index(min(t1))]
Y_mn = y[t1.index(min(t1))]
X_mx = x[t2.index(max(t2))]
Y_mx = y[t2.index(max(t2))]
a = [] * 4
clusters(t, x, y, X_mn,Y_mn, X_mx,Y_mx, key, min_iteration, max_iteration, a)
plt.title("Iris Dataset: Bisecting Min-Max", fontsize = 12)
#plt.scatter(x, y, s=1, c="black")
end = time.time()
print("\nExecution time:", end-start)
plt.show()
