# Array with Array
# Array with Scalars
# Universal Array Functions

import numpy as np
arr = np.arange(0,11)
print(arr)          #[ 0  1  2  3  4  5  6  7  8  9 10]

print('\n','*************ARRAY WITH ARRAY OPERATIONS*****************','\n')

#ADD
print(arr+arr)      #[ 0  2  4  6  8 10 12 14 16 18 20]
#SUBTRACT
print(arr-arr)      #[0 0 0 0 0 0 0 0 0 0 0]
#MULTIPLY
print(arr*arr)      #[  0   1   4   9  16  25  36  49  64  81 100]
#DIVIDE
print(arr/arr)
# RuntimeWarning: invalid value encountered in true_divide
#   print(arr/arr)
# [nan  1.  1.  1.  1.  1.  1.  1.  1.  1.  1.]

print('\n','*************ARRAY WITH SCALAR OPERATIONS**************','\n')
#Numpy broadcasts that scalar number to every element in the array
#ADD
print(arr+100)      #[100 101 102 103 104 105 106 107 108 109 110]
#SUBTRACT
print(arr-100)      #[-100  -99  -98  -97  -96  -95  -94  -93  -92  -91  -90]
#MULTIPLY
print(arr*100)      #[   0  100  200  300  400  500  600  700  800  900 1000]
#EXPONENTS
print(arr**2)      #[  0   1   4   9  16  25  36  49  64  81 100]

print('\n','*************UNIVERSAL ARRAY FUNCTIONS**************','\n')
#SQUARE ROOT
print(np.sqrt(arr))
# [0.         1.         1.41421356 1.73205081 2.         2.23606798
#  2.44948974 2.64575131 2.82842712 3.         3.16227766]
print('\n','***********************************','\n')
#EXPONENTS
print(np.exp(arr))
# [1.00000000e+00 2.71828183e+00 7.38905610e+00 2.00855369e+01
#  5.45981500e+01 1.48413159e+02 4.03428793e+02 1.09663316e+03
#  2.98095799e+03 8.10308393e+03 2.20264658e+04]
print('\n','***********************************','\n')

#TRIGNOMETRIC SIN FUNCTION
print(np.sin(arr))
# [ 0.          0.84147098  0.90929743  0.14112001 -0.7568025  -0.95892427
#  -0.2794155   0.6569866   0.98935825  0.41211849 -0.54402111]
print('\n','***********************************','\n')

#LOG
print(np.log(arr))
# RuntimeWarning: divide by zero encountered in log
#   print(np.log(arr))
# [      -inf 0.         0.69314718 1.09861229 1.38629436 1.60943791
#  1.79175947 1.94591015 2.07944154 2.19722458 2.30258509]
print('\n','***********************************','\n')

#MAX
print(np.max(arr))      #10
print(arr.max())        #10


