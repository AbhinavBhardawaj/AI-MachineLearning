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

