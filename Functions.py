import numpy as np
def savefun(a):
    np.save('files.npy',a)
    print('file saved')
def loadfun(a):
    ar=np.load('files.npy')
    print('file loaded')
def reshapefun(a):
    x=a.reshape(p,q,r)
    print('arr reshaped')
    print(x)
def transposefun(a):
    b=np.transpose(a.reshape(p,q,r))
    print('array transposed')
    print(b)
def ravelfun(a):
    x=a.ravel('F')
    print(x)
def broadcastingfun(a):
    x=arr*10
    print('arr broadcasting')
    b=a.reshape(p,q,r)
    y=b.mean(1)
    print(y)
    print(x)
def squeezefun(a):
    b=a.reshape(p,q,r)
    x=np.squeeze(b).shape
    print('squeeze')
    print(x)
if __name__=="__main__":
    n=int(input('enter size of array'))
    p=int(input('enter no of matrices to be divided'))
    q=int(input('enter row size'))
    r=int(input('enter col size'))
    print('1.load 2.reshape 3.transposefun 4.ravelfun 5.broadcastingfun 6.squeezefun 7.savefun')
    a=np.arange(n)
    print(a)
    while(1):
        ch=int(input("Enter Choice:"))
        if(ch==1):
            loadfun(a)
        elif(ch==2):
            reshapefun(a)
        elif(ch==3):
            transposefun(a)
        elif(ch==4):
            ravelfun(a)
        elif(ch==5):
            broadcastingfun(a)
        elif(ch==6):
            squeezefun(a)
        elif(ch==7):
            savefun(a)
        else:
            break