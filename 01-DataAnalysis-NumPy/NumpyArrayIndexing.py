print('\n','*************NUMPY INDEXING AND SELECTION*****************','\n')

import numpy as np

arr = np.arange(0,11)
print(arr)          #[ 0  1  2  3  4  5  6  7  8  9 10]
print(arr[8])       # 8
print(arr[1:5])     #[1 2 3 4]
print(arr[0:6])     #[0 1 2 3 4 5]
print(arr[5:])      #[ 5  6  7  8  9 10]

print('\n','*************ARRAY VALUE BROADCASTING*****************','\n')

arr[0:5] = 100
print(arr)          #[100 100 100 100 100   5   6   7   8   9  10]

print('\n','*************ARRAY SLICING*****************','\n')
#Reset the array
arr = np.arange(0,11)
print(arr)          #[ 0  1  2  3  4  5  6  7  8  9 10]

slice_of_arr = arr[0:6]
print(slice_of_arr)         #[0 1 2 3 4 5]

slice_of_arr[:] = 99
print(slice_of_arr)         #[99 99 99 99 99 99]

print(arr)                  #[99 99 99 99 99 99  6  7  8  9 10]
#Slicing of array not only changed the sliced array, but also the original array
#Data is not copied, its just a view of the original array. The reason Numpy does that is to
#avoid memory issues of very large arrays. Numpy doesn't automatically set copies of the arrays.

print('\n','*************COPYING ARRAY*****************','\n')
arr_copy = arr.copy()
print(arr_copy)             #[99 99 99 99 99 99  6  7  8  9 10] -->Copied Array

print(arr)                  #[99 99 99 99 99 99  6  7  8  9 10] -->Original Array

print('\n','*************************************','\n')

#Now Array broadcasting will only affect the copied array and original array stays the same.
arr_copy[:] = 100
print(arr_copy)             #100 100 100 100 100 100 100 100 100 100 100]

print(arr)                  #[99 99 99 99 99 99  6  7  8  9 10]

print('\n','*************INDEXING 2-D ARRAY- MATRICES*****************','\n')

arr_2d = np.array([[5,10,15],[20,25,30],[35,40,45]])
print(arr_2d)
# [[ 5 10 15]
#  [20 25 30]           -->2-D Matrix
#  [35 40 45]]

#There are 2 general formats for grabbing element from 2-D Array or Matrix
#1. Double bracket format
#2. Single bracket format with a comma
print('\n','*************DOUBLE BRACKET FORMAT*****************','\n')
# print(arr_2d[row][col])
print(arr_2d[0])            #[ 5 10 15]
print(arr_2d[0][0])         #5
print(arr_2d[1][1])         #25
print(arr_2d[2][1])         #40

print('\n','*************SINGLE BRACKET WITH COMMA FORMAT*****************','\n')
#print(arr_2d[row,col])
print(arr_2d[2,1])          #40
print(arr_2d[1,1])          #25
print(arr_2d[0,0])          #5

print('\n','*************GRAB SECTIONS OF 2-D ARRAY USING SLICING*****************','\n')
#Grab everything upto row2, from col1 onwards
print(arr_2d[:2,1:])
# [[10 15]
#  [25 30]]
print('\n','*************************************','\n')
print(arr_2d[2:,:2])
#[[35 40]]

print('\n','*************CONDITIONAL SELECTION*****************','\n')
arr = np.arange(1,11)
print(arr)

print('\n','*************************************','\n')

#Take this array and combine with comparison operators and get boolean array out of it
print(arr > 5)          #[False False False False False  True  True  True  True  True]

bool_arr = arr > 5
print(bool_arr)

print('\n','*************************************','\n')

print(arr[bool_arr])    #[ 6  7  8  9 10] --> Only returns instances where boolean array is True

print('\n','*************************************','\n')

#This all can be done in one step
print(arr[arr>5])       #[ 6  7  8  9 10]
print('\n','*************************************','\n')

#Get all elements of the array that are less than 3
print(arr[arr<3])       #[1 2]

print('\n','*************************************','\n')

arr_2d = np.arange(50).reshape(5,10)
print(arr_2d)

# [[ 0  1  2  3  4  5  6  7  8  9]
#  [10 11 12 13 14 15 16 17 18 19]
#  [20 21 22 23 24 25 26 27 28 29]
#  [30 31 32 33 34 35 36 37 38 39]
#  [40 41 42 43 44 45 46 47 48 49]]

print('\n','*************************************','\n')

print(arr_2d[1:3,3:5])
# [[13 14]
#  [23 24]]