import time
import matplotlib.pyplot as plt
import random 
import numpy as np
def mergeSort(arr):
    if len(arr) > 1:
        mid = len(arr)//2
        L = arr[:mid]
        R = arr[mid:]
        mergeSort(L)
        mergeSort(R)
        
        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i] <= R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
            
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
 
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

if __name__ == '__main__':
    x_axis = []
    y_axis = []
    for k in range(0,2000,100):
        arr = np.random.randint(0,2000,k*100)
        start = time.time()
        mergeSort(arr)
        x_axis.append(k*100)
        y_axis.append(round(time.time()-start,6))
        
    y_bestaxis = [] 
    for val in range(0,2000,100):
        best = np.arange(val*100)
        start = time.time()
        mergeSort(best)
        y_bestaxis.append(round(time.time()-start,6))
      
    y_worstaxis = []
    for val in range(0,2000,100):
        worst = np.arange(val*100,0,-1)
        start = time.time()
        mergeSort(worst)
        y_worstaxis.append(round(time.time()-start,6))
        
    plt.plot(x_axis,y_axis,marker="o",label="average_case")
    plt.plot(x_axis,y_bestaxis,marker="o",label="best_case")
    plt.plot(x_axis,y_worstaxis,marker="o",label="worst_case")
    
    plt.legend()
    plt.xlabel("SIZE")
    plt.ylabel("TIME")
    plt.savefig('mergesort.pdf')