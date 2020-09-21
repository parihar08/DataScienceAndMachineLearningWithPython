import numpy as np
import pandas as pd

from numpy.random import randn

df = pd.DataFrame(randn(5,4),['A','B','C','D','E'],['W','X','Y','Z'])
print(df)
#           W         X         Y         Z
# A  2.706850  0.628133  0.907969  0.503826
# B  0.651118 -0.319318 -0.848077  0.605965
# C -2.018168  0.740122  0.528813 -0.589001
# D  0.188695 -0.758872 -0.933237  0.955057
# E  0.190794  1.978757  2.605967  0.683509

print('\n','***************CONDITIONAL SELECTION**********************','\n')
#Pandas can perform Conditional Selection using bracket notation

print(df > 0)       #We will get boolean value True where Data Frame is greater than 0, False otherwise
#        W      X      Y      Z
# A   True  False  False   True
# B   True  False   True  False
# C  False   True  False   True
# D  False   True  False  False
# E  False  False   True   True
print('\n','*************************************','\n')

boolser = df > 0
print(boolser)
#        W      X      Y      Z
# A   True   True  False  False
# B  False   True   True  False
# C  False   True   True   True
# D   True   True   True   True
# E  False  False  False  False

print('\n','*************************************','\n')
#Pass in this boolser to the original Data Frame

print(df[boolser])
#           W         X         Y         Z
# A       NaN       NaN       NaN  1.017543
# B  0.101887       NaN       NaN  0.484575
# C       NaN  0.471359  0.324839       NaN     --> We get back value where boolser id True
# D       NaN  0.041630       NaN  0.116416     --> We get back NULL(Nan) where boolser is False
# E  1.370273  0.084122       NaN       NaN

print('\n','*************************************','\n')
# Usually we will write everything in one step
print(df[df > 0])
#           W         X         Y         Z
# A  1.272501       NaN  0.555908  1.591373
# B       NaN       NaN       NaN  1.013046
# C  1.090054  0.048139  0.303000  1.601853
# D  0.785253       NaN  0.325957       NaN
# E  0.559905       NaN       NaN       NaN

print('\n','***************PASS IN COLUMNS TO A DATAFRAME**********************','\n')
print(df['W'] > 0)
# A     True
# B    False
# C    False    --> We get back a Series linked to the actual index
# D     True
# E     True
# Name: W, dtype: bool

print('\n','*************************************','\n')

print(df['W'])
# A    0.029783
# B   -1.483095
# C   -0.233730
# D    1.039899
# E    0.090538
# Name: W, dtype: float64


print('\n','*************PASS IN SERIES TO A DATAFRAME************************','\n')
#We can use this series of Boolean values corresponding to Rows to filter out rows based of a column's
#value. We can pass the series into a Data Frame using a bracket notation
#This type of Conditional Selection is used most often.

print(df[df['W'] > 0])      #We will only get back the rows where this happens to be True
#           W         X         Y         Z
# A  0.029783  0.043891 -0.992650  0.129923      --> We only get back Rows A,D and E
# D  1.039899 -2.792079  0.749074 -1.476125      --> We don't get back those NULL values anymore
# E  0.090538 -0.398650 -2.617360 -0.266492      --> when we pass in a Series to Data Frame

print('\n','*************GRAB ALL ROWS BASED ON A COULMN CONDITION****************','\n')
#Grab all the rows in the Data Frame where Z is less than 0

print(df)
#           W         X         Y         Z
# A -1.631115 -0.707487  1.545280 -0.713505
# B  0.986815 -1.313342  0.880466  0.376234
# C -1.133982 -0.759175 -1.526438  0.179350
# D  0.433921  0.539387  0.635493 -0.014310
# E -0.626401  0.402984 -0.767034  1.108545

print('\n','*************************************','\n')

print(df[df['Z'] < 0 ])     #We get back a DataFrame in response
#           W         X         Y         Z
# A -1.631115 -0.707487  1.545280 -0.713505
# D  0.433921  0.539387  0.635493 -0.014310

print('\n','**************PERFORM OPERATIONS ON GRABBED DATAFRAME SUBSET******************','\n')
print(df)
#           W         X         Y         Z
# A  0.800584 -0.117850  0.311403 -0.419668
# B  0.935508  0.144588  0.360184 -1.774292
# C  0.682304 -0.287874  0.079247 -0.760721
# D  0.633473 -1.500072  0.983057 -1.282609
# E -0.378255 -0.382860  0.299424  0.111508

print('\n','*************************************','\n')

resultdf = df[df['W'] > 0 ]    #We get back a DataFrame in response
print(resultdf)
#           W         X         Y         Z
# A  0.800584 -0.117850  0.311403 -0.419668
# B  0.935508  0.144588  0.360184 -1.774292
# C  0.682304 -0.287874  0.079247 -0.760721
# D  0.633473 -1.500072  0.983057 -1.282609

print('\n','*************************************','\n')

print(resultdf['X'])
# A   -0.117850
# B    0.144588
# C   -0.287874
# D   -1.500072
# Name: X, dtype: float64

print('\n','*************************************','\n')
#Instead of performing operations on grabbed dataframe on multiple steps, we can do in one step

print(df[df['W'] > 0 ]['X'])
# A   -0.117850
# B    0.144588
# C   -0.287874
# D   -1.500072
# Name: X, dtype: float64

print('\n','*************************************','\n')
#We can pass in multiple columns as well
print(df[df['W'] > 0 ][['X','Y']])
#           X         Y
# A   -0.117850  0.311403
# B    0.144588  0.360184
# C   -0.287874  0.079247
# D   -1.500072  0.983057

print('\n','***************USING MULTIPLE CONDITIONS**********************','\n')

#print(df[(df['W'] > 0 ) and (df['X'] > 1) ])

#This gives an error: The truth Value of a series is ambiguous.
#As python's and operator can not take in to account a Series of Boolean values compared to another
#and operator can only deal with single instances of boolean values instead of multiple in a Series

print(df)
#           W         X         Y         Z
# A -0.247763  0.756617 -0.969023  1.016972
# B -0.421047 -1.724760 -0.067454 -0.569156
# C  0.666838  1.180594 -0.728533 -0.001707
# D -0.007604  1.915488 -1.257560  0.698683
# E  1.181119  0.510037  0.361616 -1.250083

print('\n','***************USING & OPERATOR**********************','\n')
#We need to use & operator:
print(df[(df['W'] > 0) & (df['X'] > 1)])
#           W         X         Y         Z
# C  0.666838  1.180594 -0.728533 -0.001707
print('\n','*************************************','\n')

print(df)
#           W         X         Y         Z
# A -1.432691  0.621611 -0.944422 -1.009860
# B -0.748374 -0.124060  0.756791 -0.970578
# C  2.342440 -0.394978  2.319193  0.155555
# D -2.024179  0.359143 -1.381225  0.069798
# E -0.065556 -0.244997 -1.101553  1.672004

print('\n','***************USING OR(|) OPERATOR**********************','\n')
#We need to use & operator:
print(df[(df['W'] > 0) | (df['X'] > 1)])
#          W         X         Y         Z
# C  2.34244 -0.394978  2.319193  0.155555

print('\n','***************RESETTING THE INDEX OF A DATAFRAME*********************','\n')
df = pd.DataFrame(randn(5,4),['A','B','C','D','E'],['W','X','Y','Z'])
print(df)
#           W         X         Y         Z
# A -0.892180  1.078451 -1.118873  0.125595
# B -0.302518  0.572344 -0.484476 -1.151261
# C  0.176517  1.341832 -0.218164 -2.033256
# D  0.137744 -0.874089 -1.168799  0.185750
# E -0.597713 -0.937232 -0.181315 -0.216320

print('\n','*************************************','\n')
#Reset index to default(0,1,2,3,4.....) and our old index will become a column in our DataFrame
print(df.reset_index())
#   index         W         X         Y         Z
# 0     A -0.892180  1.078451 -1.118873  0.125595
# 1     B -0.302518  0.572344 -0.484476 -1.151261
# 2     C  0.176517  1.341832 -0.218164 -2.033256
# 3     D  0.137744 -0.874089 -1.168799  0.185750
# 4     E -0.597713 -0.937232 -0.181315 -0.216320

#This reset doesn't occur in place unless we specify it to occur by mentioning inplace=True
#df.reset_index(inplace=True)

print('\n','***************SETTING THE INDEX**********************','\n')
new_ind = 'CA NY WY OR CO'.split()                  #Returns a list
print(new_ind)      #['CA', 'NY', 'WY', 'OR', 'CO']

print('\n','*************************************','\n')

print(df)
#           W         X         Y         Z
# A -1.426661  1.397592  0.538267  0.379276
# B  1.720432  1.123839  0.246796  0.789836
# C -0.702370  1.030267  1.007012 -1.123777
# D -1.067105 -0.726935  0.931012 -0.048483
# E  0.112465 -0.143985 -0.275169 -0.581965

print('\n','*************************************','\n')

df['States'] = new_ind
print(df)
#           W         X         Y         Z States
# A -1.426661  1.397592  0.538267  0.379276     CA
# B  1.720432  1.123839  0.246796  0.789836     NY
# C -0.702370  1.030267  1.007012 -1.123777     WY
# D -1.067105 -0.726935  0.931012 -0.048483     OR
# E  0.112465 -0.143985 -0.275169 -0.581965     CO

print('\n','************COLUMN TO BE A INDEX*************************','\n')
#If we want a column to be a new index
print(df.set_index('States'))                   #Now States column is the index
#              W         X         Y         Z
# States
# CA      1.436226 -0.651440  0.384945 -1.439016
# NY      0.493831  0.040261 -0.751031 -1.403591
# WY      1.729068  0.228065 -0.169551 -0.415931
# OR      1.529943 -0.778258 -2.042563  0.231660
# CO      0.207389  2.404733 -0.028071 -0.457497

#Unless we do df.set_index('States',inplace=True), it won't retain value of the changes we set
#inplace=True has to be set if we want the changes to be permanent
print('\n','*************************************','\n')
print(df)
#           W         X         Y         Z States
# A  1.436226 -0.651440  0.384945 -1.439016     CA
# B  0.493831  0.040261 -0.751031 -1.403591     NY
# C  1.729068  0.228065 -0.169551 -0.415931     WY
# D  1.529943 -0.778258 -2.042563  0.231660     OR
# E  0.207389  2.404733 -0.028071 -0.457497     CO
