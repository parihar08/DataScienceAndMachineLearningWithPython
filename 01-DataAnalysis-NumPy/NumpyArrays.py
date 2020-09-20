#Create numPy arrays from Python objects - list

my_list = [1,2,3]
print(my_list)          #[1, 2, 3]

print('*************1-D Array****************','\n')

import numpy as np

arr = np.array(my_list)
print(arr)              #[1 2 3] - Returns back 1-D array

print('***********************************','\n')

my_mat = [[1,2,3],[4,5,6],[7,8,9]] #list of list
print(my_mat)           #[[1, 2, 3], [4, 5, 6], [7, 8, 9]]

print('*************2-D Array****************','\n')

np.array(my_mat)
print(my_mat)           #[[1, 2, 3], [4, 5, 6], [7, 8, 9]] - Returns back 2-D array

print('*************CREATE NUMPY ARRAYS*****************','\n')

#np.arange(start,stop,step) --> Similar to python range() function

arr = np.arange(0,10)
print(arr)              #[0 1 2 3 4 5 6 7 8 9]

arr = np.arange(0,11,2)
print(arr)              #[ 0  2  4  6  8 10]

print('***********************************','\n')
#Generate Arrays of all 0's
arr = np.zeros(3)
print(arr)              #[0. 0. 0.]  --> 1-D Vector

print('***********************************','\n')

arr = np.zeros((5,5))   #Pass in a tuple of the vectors we want
print(arr)

# [[0. 0. 0. 0. 0.]
#  [0. 0. 0. 0. 0.]
#  [0. 0. 0. 0. 0.]     --> 2-D Matrix
#  [0. 0. 0. 0. 0.]
#  [0. 0. 0. 0. 0.]]
print('***********************************','\n')

#Generate Arrays of all 1's
arr = np.ones(4)
print(arr)              #[1. 1. 1. 1.]  --> 1-D Vector

print('***********************************','\n')

arr = np.ones((3,4))   #Pass in a tuple of the vectors we want
print(arr)
# [[1. 1. 1. 1.]
#  [1. 1. 1. 1.]        --> 2-D Matrix
#  [1. 1. 1. 1.]]

print('***************LINSPACE********************','\n')
#Linspace returns evenly spaced numbers over a specified interval

#np.linspace(start,stop,num=10)
arr = np.linspace(0,5,10)
print(arr)
# [0.         0.55555556 1.11111111 1.66666667 2.22222222 2.77777778
#  3.33333333 3.88888889 4.44444444 5.        ]

print('***********************************','\n')

arr = np.linspace(0,9,10)
print(arr)
# [0. 1. 2. 3. 4. 5. 6. 7. 8. 9.]

print('\n','*************CREATE IDENTITY MATRIX*****************')
#Identity matrix is 2-D square matrix (no. of rows = cols) and we have a diagonal of 1's and
#everything else is 0's

arr = np.eye(4)
print(arr)
# [[1. 0. 0. 0.]
#  [0. 1. 0. 0.]        --> 2-D Matrix having a diagonal of 1's and everything else as 0's
#  [0. 0. 1. 0.]
#  [0. 0. 0. 1.]]

print('\n','*************CREATE ARRAYS OF RANDOM NUMBERS*****************','\n')

# arr = np.random.rand()
#random.rand() creates an array of the given shape we pass in and populate it with a random
# sample with a uniform distribution over 0 to 1
print('\n','**************RAND 1-D*********************','\n')
arr = np.random.rand(5)
print(arr)      #[0.75650528 0.36869207 0.7452497  0.03048825 0.89906463] --> 1-D

print('\n','**************RAND 2-D*********************','\n')
arr = np.random.rand(5,5) #We don't pass tuple here, each dimension is passed as a separate argument
print(arr)
# [[0.61253783 0.39758494 0.49912416 0.50048739 0.04807435]
#  [0.26871198 0.31486777 0.98305056 0.86855579 0.27813999]
#  [0.96504857 0.02887879 0.56986026 0.52798452 0.32359529]     --> 2-D Matrix
#  [0.23075776 0.83117526 0.42021617 0.19286346 0.69563044]
#  [0.79133756 0.04572638 0.08156427 0.77435521 0.61140931]]

print('\n','**************RANDN 1-D*********************','\n')
# arr = np.random.randn()
#random.rand() will return numbers not from a uniform distribution from 0 to 1 but instead from
#a standard normal distribution centered around 0
arr = np.random.randn(5)
print(arr)  #[-2.0405596  -0.00412444  0.30917196  0.11083328  1.83482548]  --> 1-D

print('\n','**************RANDN 2-D*********************','\n')
arr = np.random.randn(4,4 ) #We don't pass tuple here, each dimension is passed as a separate argument
print(arr)
# [[ 0.22303093 -0.05724996  1.15247661 -1.22922506]
#  [ 2.16806972  1.36770526  0.06632999  2.40821133]            --> 2-D Matrix
#  [ 0.18157308  0.05705839  0.76492356  1.96489667]
#  [-0.83719293 -1.72655164 -0.47518631 -0.92846146]]

print('\n','**************RANDINT 1-D*********************','\n')
#Returns random integers from a low to a high number
# arr = np.random.randint(low,high,size)   --> low-inclusive high-exclusive
arr = np.random.randint(1,100)
print(arr)                          #59
arr = np.random.randint(1,100,10)
print(arr)                          #[62 15 11 22 46  2 89 48 58 25]    --> 1-D

print('\n','**************ARRAY ATTRIBUTES AND METHODS*********************','\n')

arr = np.arange(25)
print(arr)
print(arr.shape)        #(25,)  -->Topic covered below
print('***********************************')
ranarr = np.random.randint(0,50,10)
print(ranarr)

print('\n','**************RESHAPE METHOD*********************','\n')
#Returns an array conataining same data of a new shape

arr = arr.reshape(5,5)
print(arr)
# [[ 0  1  2  3  4]
#  [ 5  6  7  8  9]
#  [10 11 12 13 14]
#  [15 16 17 18 19]
#  [20 21 22 23 24]]

#Since size of arr is 25, we cannot get a reshaped array having more than 25 elements
#arr = arr.reshape(5,10)
#print(arr)          #ValueError: cannot reshape array of size 25 into shape (5,10)

print('\n','**************FIND MAX AND MIN VALUES*********************','\n')
print(ranarr)           #[[10  0  9 18 38 48 35 14 38  8]
print(ranarr.max())     #48
print(ranarr.min())     #0

print('\n','**************FIND LOCATION OF MAX AND MIN VALUES*****************','\n')
print(ranarr.argmax())  #5  -->Index location of Max element(48)
print(ranarr.argmin())  #1  -->Index location of Min element(0)

print('\n','**************SHAPE OF A VECTOR*********************','\n')
print(arr.shape)    #(5, 5)     -->Shape after reshaping -->2-D
print(ranarr.shape) #(10,)

print('\n','***************DATA TYPE IN THE ARRAY*******************','\n')
print(ranarr.dtype)     #int64
print(arr.dtype)        #int64
