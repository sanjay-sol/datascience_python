import numpy as np
import statistics as stats
def mean(n):
    mean=np.mean(n)
    print("Mean:",mean)
def median(n):
    med=np.median(n)
    print("Median:",med)
def mode(n):
    mode=stats.mode(n)
    print("Mode:",mode)
def standdev(n):
    sd=np.std(n)
    print("Standard Deviation:",sd)
def variance(n):
    var=np.var(n)
    print("Variance:",var)
if __name__=='__main__':
    lists=[]
    n=int(input("Enter no:of values:"))
    print("Enter numbers:")
    for i in range(0,n):
        lists.append(int(input()))
    print("1.Mean\n2.Median\n3.Mode\n4.Standard Deviation\n5.Variance")
    while(True):
        print("Enter Choice:")
        ch=int(input())
        if ch==1:
            mean(lists)
        elif ch==2:
            median(lists)
        elif ch==3:
            mode(lists)
        elif ch==4:
            standdev(lists)
        elif ch==5:
            variance(lists)
        else:
            break