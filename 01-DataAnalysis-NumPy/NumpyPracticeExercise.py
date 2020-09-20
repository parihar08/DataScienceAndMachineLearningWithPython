import numpy as np

#Create arrays of 10 zeroes
arr = np.zeros(10)
print(arr)

print('\n','***********************************','\n')

#Create arrays of 10 ones
arr = np.ones(10)
print(arr)

print('\n','***********************************','\n')

#Create arrays of 10 fives
arr = np.ones(10)*5
print(arr)

arr = np.zeros(10)+5
print(arr)

print('\n','***********************************','\n')

#Create arrays of integers from 10 to 50
arr = np.arange(10,51)
print(arr)

print('\n','***********************************','\n')

#Create arrays of all even integers from 10 to 50
arr = np.arange(10,51,2)
print(arr)

print('\n','***********************************','\n')

#Create 3*3 matrix with values ranging from 0 to 8
arr = np.arange(9).reshape(3,3)
print(arr)

print('\n','***********************************','\n')

#Create 3*3 identity matrix
arr = np.eye(3)
print(arr)

print('\n','***********************************','\n')

#Use Numpy to generate a random number between 0 and 1
arr = np.random.rand(1)
print(arr)

print('\n','***********************************','\n')

#Use Numpy to generate a array of 25 random numbers sampled from a standard normal distribution
arr = np.random.randn(25)
print(arr)
print(arr.shape)

print('\n','***********************************','\n')

#Use Numpy to generate a 2-D array
arr = np.arange(0.01,1.01,0.01).reshape(10,10)
print(arr)
print(arr.shape)

print('\n','***********************************','\n')

arr = np.arange(1,101).reshape(10,10)/100
print(arr)
print(arr.shape)

print('\n','***********************************','\n')

arr = np.linspace(0.01,1,100)
print(arr)

print('\n','***********************************','\n')

#Create array of 20 linearly spaced points between 0 and 1
arr = np.linspace(0,1,20)
print(arr)

print('\n','**************NUMPY INDEXING AND SELECTION*********************','\n')
mat = np.arange(1,26).reshape(5,5)
print(mat)

print('\n','***********************************','\n')
print(mat[2:,1:])

print('\n','***********************************','\n')
print(mat[3,4])     #20

print('\n','***********************************','\n')
print(mat[:3,1:2])

print('\n','***********************************','\n')
print(mat[4:,])     #[[21 22 23 24 25]] -->2-D Array

print('\n','***********************************','\n')
print(mat[4,:])     #[21 22 23 24 25]   -->1-D Array

print('\n','***********************************','\n')
print(mat[-1,:])     #[21 22 23 24 25]   -->1-D Array  Negative Indexing: -1 index for last row

print('\n','***********************************','\n')
print(mat[4,])     #[21 22 23 24 25]   -->1-D Array

print('\n','***********************************','\n')
print(mat[3:,])
# [[16 17 18 19 20]         -->2-D Array
#  [21 22 23 24 25]]

print('\n','***********************************','\n')
print(mat[3:,:])
# [[16 17 18 19 20]         -->2-D Array
#  [21 22 23 24 25]]

print('\n','**************NUMPY OPERATIONS*********************','\n')
#Use Numpy to get sum of all values of mat array
print(mat.sum())        #325
print(np.sum(mat))      #325

print('\n','***********************************','\n')

#Use Numpy to get standard deviation of values in mat array
print(mat.std())        #7.211102550927978
print(np.std(mat))      #7.211102550927978

print('\n','***********************************','\n')

#Use Numpy to get sum of all columns of mat array
print(mat.sum(axis=0))      #[55 60 65 70 75]

print('\n','***********************************','\n')

#Use Numpy to get sum of all rows of mat array
print(mat.sum(axis=1))

print('\n','***********************************','\n')