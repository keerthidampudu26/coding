import numpy as np
arr=np.array([1,2,np.nan,5])
print("mean ignoring NaN:",np.nanmean(arr))
print("sum:",np.sum(arr))
print("sd ignoring nan",np.std(arr[~np.isnan(arr)]))

