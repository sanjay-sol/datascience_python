import numpy as np 
arr=np.array([[-8,6,-1],[-7,np.nan,0],[-3,0,np.nan]]) 
print(arr) 
arr1=np.any(arr) 
print('Any non-zero ele:',arr1) 
arr2=np.isfinite(arr)
print('Finite:\n',arr2)