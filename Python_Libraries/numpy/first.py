import numpy as np

a = np.array([1,2,3]) # vector
print(a)

# 2d array
b = np.array([[1,2,3],[4,5,6]]) # matrix
print(b)

# 3d array
c = np.array([[[1,2],[3,4]],[[5,6],[7,8]]]) # tensor
print(c)

# dtype

d = np.array([1,2,3],dtype=float)
print(d)

e = np.array([1,2,3],dtype = complex)
print(e)

# np.arange, gives value in the given range excludes the stop value, also u can use step value

f = np.arange(1,12)
print(f)

f = np.arange(1,12,2) 
print(f)

# np.reshape, this is used to reshape a matrix into given dimensions
# dimensions multiplication should be equal to total elements or else ValueError will be raised

g = np.arange(2,10).reshape(2,4)
print(g)

g = np.arange(2,10).reshape(4,2)
print(g)

# g = np.arange(2,10).reshape(2,5)
# print(g) will raise ValueError

# Array intialisation techniques

# np.ones and np.zeroes

h = np.ones((3,4))
print(h)

h = np.zeros((4,3))
print(h)

# np.random it generates a number between 0 and 1

i = np.random.random((3,4))
print(i)

# np.linspace(start, end , no of partitions or no of elements) generates the array includes start and end
# also generates an array of evenly spaced numbers over a specified interval.

j = np.linspace(-3,4,6)
print(j)

print(np.identity(4))

# np.diag has 2 behaviours extracts a diagonal from 2d matrix 
# or constructs a diagonal matrix from a 1D array

mat = np.array([[1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]])

print(np.diag(mat,k = 0))
print(np.diag(mat,k = 1))
print(np.diag(mat,k = -1))

arr = np.array([10, 20, 30])
print(np.diag(arr))

# Numpy attributes

a1 = np.arange(10)
a2 = np.arange(12,dtype = float).reshape(3,4)
a3 = np.arange(8).reshape(2,2,2)

# ndim helps us to identify number of dimensions
print(a1.ndim)
print(a2.ndim)
print(a3.ndim) 

# Note: in 3d array (2,2,2) in this 1st parameter means how many 2d arrays are there
# then the next two parameters says the no of rows and no of columns

# shape() no of items in each dimension

print(a1.shape)
print(a2.shape)
print(a3.shape)

# size() total no of elements

print(a1.size)
print(a2.size)
print(a3.size)

# itemsize() each item occupies how many bytes in memory

print(a1.itemsize)
print(a2.itemsize)
print(a3.itemsize)

# dtype

print(a1.dtype)
print(a2.dtype)
print(a3.dtype)


# Changing Datatype

# astype
a3 = a3.astype(np.int32) # a3.astype(np.int32) does not modify a3 in place; it returns a brand-new array copy. 
print(a3.dtype)

# Array operations

a1 = np.arange(12).reshape(3,4)
a1 = np.arange(12,24).reshape(3,4)

# Scalar Operations, we can perform every arithmetic, relational operations

# Arithmetic Operations
print(a1*2)
print(a1**2)
print(a1+5)

# Relational operations
print(a1>5)
print(a1>25)
print(a2 == 15)


# Vector Operations takes place b/w np arrays having same shape 

# Arithmetic operations

print(a1 + a2)
print(a1 * a2)


# Array Functions

a1 = np.random.random((3,3))
a1 = np.round(a1*100)
print(a1)

# max/min/sum/prod
# axis => 0 -> col, 1 -> row

print(np.max(a1))
print(np.min(a1))
print(np.sum(a1))
print(np.prod(a1))

print(np.max(a1,axis = 0))
print(np.max(a1,axis = 1))

print(np.sum(a1,axis = 0))
print(np.sum(a1,axis=1))

# mean/median/std/var --> even here u can use to axis to find for a particular row or col

print(np.mean(a1))
print(np.median(a1))
print(np.std(a1))
print(np.var(a1))

# dot product

a2 = np.arange(12).reshape(3,4)
a3 = np.arange(12,24).reshape(4,3)

print(np.dot(a2,a3))

# log/exp
print(np.log(a2))
print(np.exp(a3))

# round/floor/ceil

a4 = np.random.random((3,4))*100

print(np.round(a4))
print(np.floor(a4))
print(np.ceil(a4))


# Indexing and Slicing

a1 = np.arange(10)
a2 = np.arange(12).reshape(3,4)
a3 = np.arange(8).reshape(2,2,2)

# Indexing
print(a1[0])

print(a2[1,0]) # arr[row,col]
print(a3)

''' [[[0 1]
      [2 3]] => arr[which 2d does the given element exist, row, col]

     [[4 5]
      [6 7]]]'''

print(a3[1,0,1])
print(a3[1,1,1])

# lets create a 4d and then do indexing

a4 = np.arange(24).reshape(2,3,2,2) # this means there are 2 elements in 4d matrix which contains 
# 3 3d matrix of 2 rows and 2 cols
print(a4)

'''
[[[[ 0  1]
   [ 2  3]]

  [[ 4  5]
   [ 6  7]]

  [[ 8  9]
   [10 11]]]


 [[[12 13]
   [14 15]]

  [[16 17]
   [18 19]]

  [[20 21]
   [22 23]]]]
'''
print(a4[1,2,0,1]) 
'''=> the 1 means go to the 3d matrix where the num 21 is there then 2 means go 
to the 2d matrix present in row 2 and then extract the element present in 0th row, ist col
'''

# Slicing

print(a1[2:5]) # for 1d similar to python lists

# for 2D syntax is arr[row number,:number of columns] this is to derive a row
print(a2)
'''
[[ 0  1  2  3]
 [ 4  5  6  7]
 [ 8  9 10 11]]
'''

print(a2[0,:])
print(a2[0,:3])

# To derive a specific column syntax => arr[start row:end row,column number]
print(a2[:,2])
print(a2[1:,2])
print(a2[:2,2])

# Now if I want to print [[ 5  6], [ 9 10]]
print(a2[1:,1:3])

# Now to get [[ 0  3], [ 8 11]]
print(a2[::2,::3]) # selects all the row and cols but in rows skip one and in cols skips 2 
# to get the alter elements

# Now for [[ 1  3], [ 9 11]]
print(a2[::2,1::2])

# To get [[4,7]]
print(a2[1:2,::3]) # or print(a2[1,::3])

# To get [[1 2 3], [5 6 7]]
print(a2[:2,1:])

# for 3D
a3 = np.arange(27).reshape(3,3,3)
print(a3)
'''
[[[ 0  1  2]
  [ 3  4  5]
  [ 6  7  8]]

 [[ 9 10 11]
  [12 13 14]
  [15 16 17]]

 [[18 19 20]
  [21 22 23]
  [24 25 26]]]
'''

print(a3[1])
print(a3[::2])

# To get [3 4 5]
print(a3[0,1,:])

# To get [10 13 16]
print(a3[1,:,1])

# To get [[22 23], [25 26]]
print(a3[2,1:,1:])

# To get [[ 0  2], [18 20]]
print(a3[::2,0,::2])

# Iteration on Numpy Array

# a1
''' 
[0 1 2 3 4 5 6 7 8 9]
'''
for i in a1:
    print(i) # gives all the elements

# a2
'''
[[ 0  1  2  3]
 [ 4  5  6  7]
 [ 8  9 10 11]]
'''
for i in a2:
    print(i) # gives all the rows

for i in np.nditer(a2):
    print(i)

# a3
'''
[[[ 0  1  2]
  [ 3  4  5]
  [ 6  7  8]]

 [[ 9 10 11]
  [12 13 14]
  [15 16 17]]

 [[18 19 20]
  [21 22 23]
  [24 25 26]]]
'''

for i in a3:
    print(i) # gives all the matrix

for i in np.nditer(a3): 
    print(i)

# Note: np.nditer(<arr>) helps to get the all the elements instead of rows or matrix, 
# works for any dimension

# Shaping

# Transpose
# a2
'''
[[ 0  1  2  3]
 [ 4  5  6  7]
 [ 8  9 10 11]]
'''
print(np.transpose(a2))
print(a2.T) # Above both the methods are use to transpose a matrix

# ravel, this converts any dim matrix to 1D arr
print(a3.ravel())

# Stacking, can perform over n arrays but of same dimension

a4 = np.arange(12).reshape(3,4)
a5 = np.arange(12,24).reshape(3,4)

# Horizontal stacking
print(np.hstack((a4,a5)))

# Vertical stacking
print(np.vstack((a4,a5)))


# Splitting

# hsplit(arr,no of equal divisions)
print(np.hsplit(a4,2))

# vsplit
a5 = np.arange(12,24).reshape(4,3)
print(np.vsplit(a5,2))