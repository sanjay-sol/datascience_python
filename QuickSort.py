def quick_Sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_Sort(left) + middle + quick_Sort(right)
if __name__ == '__main__':
    x_axis = []
    y_axis = []
    for k in range(0,2000,100):
        arr = np.random.randint(0,2000,k*100)
        start = time.time()
        quick_Sort(arr)
        x_axis.append(k*100)
        y_axis.append(round(time.time()-start,6))
        
    y_bestaxis = [] 
    for val in range(0,2000,100):
        best = np.arange(val*100)
        start = time.time()
        quick_Sort(best)
        y_bestaxis.append(round(time.time()-start,6))  
    y_worstaxis = []
    for val in range(0,2000,100):
        worst = np.arange(val*100,0,-1)
        start = time.time()
        quick_Sort(worst)
        y_worstaxis.append(round(time.time()-start,6))
    plt.plot(x_axis,y_axis,marker="o",label="average_case")
    plt.plot(x_axis,y_bestaxis,marker="o",label="best_case")
    plt.plot(x_axis,y_worstaxis,marker="o",label="worst_case")
    plt.legend()
    plt.xlabel("SIZE")
    plt.ylabel("TIME")