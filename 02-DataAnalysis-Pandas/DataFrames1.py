#Data Frames are the main tool when working with Pandas
#Data Frames is a bunch of Series that share the same index
#Data Frames are fancy index markers on top of a NumPy array

import numpy as np
import pandas as pd

from numpy.random import randn

np.random.seed(101)

print('\n','***************DATA LIST**********************','\n')
#df = pd.DataFrame(data=,index=,columns=
df = pd.DataFrame(randn(5,4),['A','B','C','D','E'],['W','X','Y','Z'])
print(df)
#           W         X         Y         Z
# A  2.706850  0.628133  0.907969  0.503826
# B  0.651118 -0.319318 -0.848077  0.605965
# C -2.018168  0.740122  0.528813 -0.589001
# D  0.188695 -0.758872 -0.933237  0.955057
# E  0.190794  1.978757  2.605967  0.683509

print('\n','**********GRAB ELEMENT FROM DATA LIST USING INDEXING AND SELECTION************','\n')

print('\n','**************SELECTING COLUMNS***********************','\n')
print(df['W'])  #This returns 'W' column which looks like a series
# A    2.706850
# B    0.651118
# C   -2.018168
# D    0.188695
# E    0.190794
# Name: W, dtype: float64

print('\n','*************************************','\n')
print(type(df['W']))        #<class 'pandas.core.series.Series'>

print('\n','*************************************','\n')
print(type(df))             #<class 'pandas.core.frame.DataFrame'>

print('\n','*************************************','\n')
#We can also use this SQL like notation to get values from a particular column
print(df.W)     #This returns 'W' column which looks like a series
# A    2.706850
# B    0.651118
# C   -2.018168
# D    0.188695
# E    0.190794
# Name: W, dtype: float64
print('\n','***************TO HAVE MULTIPLE COLUMNS BACK**********************','\n')
#Pass in a list of columns --> We get back a data frame
print(df[['W','Z']])
#           W         Z
# A  2.706850  0.503826
# B  0.651118  0.605965
# C -2.018168 -0.589001
# D  0.188695  0.955057
# E  0.190794  0.683509

print('\n','***************ADD A NEW COLUMN**********************','\n')
#print(df['new'])         #KeyError: 'new' -->As 'new' column doesn't exist in our data frame

df['new'] = df['W'] + df['Y']
print(df)
#           W         X         Y         Z       new
# A  2.706850  0.628133  0.907969  0.503826  3.614819
# B  0.651118 -0.319318 -0.848077  0.605965 -0.196959
# C -2.018168  0.740122  0.528813 -0.589001 -1.489355
# D  0.188695 -0.758872 -0.933237  0.955057 -0.744542
# E  0.190794  1.978757  2.605967  0.683509  2.796762


print('\n','**************DROP A COLUMN***********************','\n')
#df.drop('new')          KeyError: "['new'] not found in axis"
print(df.drop('new',axis=1))
#           W         X         Y         Z
# A  2.706850  0.628133  0.907969  0.503826
# B  0.651118 -0.319318 -0.848077  0.605965
# C -2.018168  0.740122  0.528813 -0.589001
# D  0.188695 -0.758872 -0.933237  0.955057
# E  0.190794  1.978757  2.605967  0.683509

print('\n','*************************************','\n')
print(df)     #-->By default, df.drop() doesn't impact the original data frame
#           W         X         Y         Z       new
# A  2.706850  0.628133  0.907969  0.503826  3.614819
# B  0.651118 -0.319318 -0.848077  0.605965 -0.196959
# C -2.018168  0.740122  0.528813 -0.589001 -1.489355
# D  0.188695 -0.758872 -0.933237  0.955057 -0.744542
# E  0.190794  1.978757  2.605967  0.683509  2.796762

print('\n','*************************************','\n')
#We need to specify inplace=True if we want to make changes to the original data frame
df.drop('new',axis=1,inplace=True)
print(df)
#           W         X         Y         Z
# A  2.706850  0.628133  0.907969  0.503826
# B  0.651118 -0.319318 -0.848077  0.605965
# C -2.018168  0.740122  0.528813 -0.589001
# D  0.188695 -0.758872 -0.933237  0.955057
# E  0.190794  1.978757  2.605967  0.683509

print('\n','***************ANOTHER WAY BY ASSIGNING BACK**********************','\n')
# df = df.drop('new',axis=1)
# print(df)
#           W         X         Y         Z
# A  2.706850  0.628133  0.907969  0.503826
# B  0.651118 -0.319318 -0.848077  0.605965
# C -2.018168  0.740122  0.528813 -0.589001
# D  0.188695 -0.758872 -0.933237  0.955057
# E  0.190794  1.978757  2.605967  0.683509

print('\n','***************DROP A ROW**********************','\n')
print(df.drop('E',axis=0))     #By Default axis=0 even if we do not pass
#           W         X         Y         Z
# A  2.706850  0.628133  0.907969  0.503826
# B  0.651118 -0.319318 -0.848077  0.605965
# C -2.018168  0.740122  0.528813 -0.589001
# D  0.188695 -0.758872 -0.933237  0.955057

print('\n','*************************************','\n')
print(df)
#           W         X         Y         Z
# A  2.706850  0.628133  0.907969  0.503826
# B  0.651118 -0.319318 -0.848077  0.605965
# C -2.018168  0.740122  0.528813 -0.589001
# D  0.188695 -0.758872 -0.933237  0.955057
# E  0.190794  1.978757  2.605967  0.683509

print('\n','*************************************','\n')
print(df.shape)     #(5, 4)  --> Its a tuple :0 index of tuple is row and 1 index is column

print('\n','**************SELECTING ROWS***********************','\n')
#First way to grab a row based on Row Label
print(df.loc['A'])            #This takes in a label(row) we want and returns a Series

# W    2.706850
# X    0.628133
# Y    0.907969
# Z    0.503826
# Name: A, dtype: float64

print('\n','*************************************','\n')
#Second way to grab a row based on index position even if our access are labelled by string
# print(df.iloc[0])
# W    2.706850
# X    0.628133             -->Using index=0 for First Row - 'A', 1 for 'B', 2 for 'C' ...
# Y    0.907969
# Z    0.503826
# Name: A, dtype: float64


print('\n','**************SELECTING SUBSETS OF ROWS AND COLUMNS***********************','\n')
#Using Comma notation
print(df.loc['B','Y'])  #Returns element at Row 'B' and Column 'Y':  -0.8480769834036315

print('\n','*************************************','\n')

#Subset of A,B rows and W,Y columns
print(df.loc[['A','B'],['W','Y']])
#           W         Y
# A  2.706850  0.907969
# B  0.651118 -0.848077