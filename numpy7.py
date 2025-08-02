import numpy as np
arr=np.array([1,2,3,np.nan,5])
print("ignoring nan ",np.nanmean(arr))
print("sum",np.sum(arr))
