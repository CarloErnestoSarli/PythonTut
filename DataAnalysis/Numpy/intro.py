# import

import numpy as np

# NdArrays (Multidimensional arrays)
# Random data 

data = np.random.randn(2, 3)    
# creates a 2 dimensional array with 3 random elements per dimensions

# find array dimensions
print (data.shape)
# output (2, 3)

# just number of dimensions
print(data.ndim)
# output: 2

# find type of data 
print(data.dtype)
# output: float64

# make array from list 
list1 = [1, 4, 3, 8]

arr1 = np.array(list1)
print(arr1)
# output:  [1 4 3 8]

# nested lists are converted to multidimensional arrays
# note they need to be same length
list2 = [[1, 4, 3, 8], [48, 9, 39, 3]]
arr2 = np.array(list2)
print(arr2)
# output:  [[ 1  4  3  8][48  9 39  3]] 

print(arr2.ndim)
# output: 2

# create array and fill with 0s
zeros = np.zeros(5)
print (zeros)
# [0. 0. 0. 0. 0.]

# create array and fill with 1s
ones = np.ones(5)
print (ones)
# [1. 1. 1. 1. 1.]

# add dimensions 

zeros2D = np.zeros((5, 2))
print (zeros2D) 
# [[0. 0.]
#  [0. 0.]
#  [0. 0.]
#  [0. 0.]
#  [0. 0.]]

# create array of sequential numbers in range
seq = np.arange(10)
print (seq)
# [0 1 2 3 4 5 6 7 8 9]


# specify data type
arrWType = np.array([1, 2, 3], dtype=np.float64)
print (arrWType.dtype)
# float64

# cast array 
arrWDiffType = arrWType.astype(np.int32)
print (arrWDiffType.dtype)
# int32 

''' ARITHMETIC '''

# arr1 [1 4 3 8]
sum = arr1 + arr1 
print (sum)
#[ 2  8  6 16]

times = arr1 * arr1 
print (times)
#[ 1 16  9 64]

minus = arr1 - arr1 
print (minus)
#[0 0 0 0]

div = arr1 / arr1
print (div)
#[1. 1. 1. 1.]

ex = np.exp(arr1)
print (ex)
# [2.71828183e+00 5.45981500e+01 2.00855369e+01 2.98095799e+03]

sqrt = np.sqrt(ex)
print (sqrt)
# [ 1.64872127  7.3890561   4.48168907 54.59815003]


''' indexing and slicing '''

print (arr1[2])
# 3

print (arr1[2:4])
# [3 8]

# avoid aliasing by using .copy()
sli = arr1[0:2].copy()
print (sli)
# [1 4]

sli[0] = 12
print (sli)
# [12  4]

print (arr1)
# [1 4 3 8]

# no aliasing


''' Transposing and reshaping '''

tr = np.arange(10).reshape(2,5)
# create array of 10 el 0 to 9 and reshape into a 2d array of 5 el
print (tr)
# [[0 1 2 3 4]
#  [5 6 7 8 9]]


# invert axis
print (tr.T)
# [[0 5]
#  [1 6]
#  [2 7]
#  [3 8]
#  [4 9]]


