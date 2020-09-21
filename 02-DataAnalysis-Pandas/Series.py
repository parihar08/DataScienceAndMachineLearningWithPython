#Series is built on top of NumPy array object
#Difference between NumPy array and Series is that Series can have Access Labels, means Series can be
#indexed by a label

import numpy as np
import pandas as pd

labels = ['a','b','c']      #Python List
my_data = [10,20,30]        #Python List

arr = np.array(my_data)     #NumPy Array
d = {'a':10,'b':20,'c':30}  #Python Dictionary

print('\n','***************SERIES**********************','\n')

print(pd.Series(data=my_data))
# 0    10
# 1    20
# 2    30
# dtype: int64

print('\n','***************LABELLED INDEX SERIES**********************','\n')

#We can specify what we want an index to be in a Pandas Series
print(pd.Series(data=my_data,index=labels))
# a    10
# b    20
# c    30
# dtype: int64

print('\n','*************************************','\n')
#Since data and index are in order, we can simply say: mydata,labels
print(pd.Series(my_data,labels))
# a    10
# b    20
# c    30
# dtype: int64

print('\n','****************CREATE A SERIES USING NUMPY ARRAY*********************','\n')
#Another way to create Series is by Passing NumPy Array
print(pd.Series(arr))
# 0    10
# 1    20
# 2    30
# dtype: int64

print('\n','*************************************','\n')
#Using labels with NumPy array
print(pd.Series(arr,labels))
# a    10
# b    20
# c    30
# dtype: int64

print('\n','****************CREATE A SERIES BY PASSING DICTIONARY*********************','\n')
#Pandas will take keys of a dictionary as index and set the value of dictionary to the data point
print(pd.Series(d))
# a    10
# b    20
# c    30
# dtype: int64

print('\n','**************FLEXIBILITY OF PANDA SERIES***********************','\n')
#Panda Series can hold a variety of object types, that's a difference from NumPy Array
#It can hold data as Numbers/Strings/References to built-in functions
print(pd.Series(data=labels))
# 0    a
# 1    b
# 2    c
# dtype: object

print('\n','*************************************','\n')
#It can hold data as Numbers/Strings/References to built-in functions
print(pd.Series(data=[sum,print,len]))
# 0      <built-in function sum>
# 1    <built-in function print>
# 2      <built-in function len>
# dtype: object

print('\n','**************USING INDEXES OF PANDA SERIES***********************','\n')
#It works like just a hash table or a dictionary
ser1 = pd.Series([1,2,3,4],['USA','CAN','IND','AUS'])
print(ser1)
# USA    1
# CAN    2
# IND    3
# AUS    4
# dtype: int64

print('\n','*************************************','\n')
ser2 = pd.Series([1,2,5,4],['USA','CAN','UK','AUS'])
print(ser2)
# USA    1
# CAN    2
# UK     5
# AUS    4
# dtype: int64

print('\n','****************GRAB INFO FROM A SERIES*********************','\n')
print(ser1['USA'])      #1          --> Here, Index is a String
print(ser1['IND'])      #3          --> Pass index labels and get back data corresponding to them
print(ser2['USA'])      #1
#print(ser2['IND'])      #KeyError: 'IND'
print(ser2['UK'])       #5

print('\n','*************************************','\n')
ser3 = pd.Series(data=labels)
print(ser3)
# 0    a
# 1    b
# 2    c
# dtype: object

print('\n','*************************************','\n')
print(ser3[0])          #a          --> Here, Index is an Integer
print(ser3[1])          #b
print(ser3[2])          #c

print('\n','****************ADDING SERIES*********************','\n')
print(ser1+ser2)
# AUS    8.0    -->4(Ser1)+4(Ser2)=8
# CAN    4.0    -->2(Ser1)+2(Ser2)=4
# IND    NaN    -->IND is only present in Ser1. Should be present in both series to perform ADD
# UK     NaN    -->UK is only present in Ser2. Should be present in both series to perform ADD
# USA    2.0    -->1(Ser1)+1(Ser2)=2
# dtype: float64

#Intergers are converted into Floats whenever we are performing any operations using Pandas Series

