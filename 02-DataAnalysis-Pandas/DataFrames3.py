import numpy as np
import pandas as pd

from numpy.random import randn

#Index Levels
outside = ['G1','G1','G1','G2','G2','G2']
inside = [1,2,3,1,2,3]
hier_index = list(zip(outside,inside))
print(hier_index)       #[('G1', 1), ('G1', 2), ('G1', 3), ('G2', 1), ('G2', 2), ('G2', 3)]

print('\n','***************MULTI INDEX DATAFRAME/INDEX HIERARCHY**********************','\n')

hier_index = pd.MultiIndex.from_tuples(hier_index)
print(hier_index)
# MultiIndex([('G1', 1),
#             ('G1', 2),
#             ('G1', 3),
#             ('G2', 1),
#             ('G2', 2),
#             ('G2', 3)],
#            )
print('\n','*************************************','\n')
df = pd.DataFrame(randn(6,2),hier_index,['A','B'])
print(df)
#              A         B
# G1 1 -0.477829  1.143890
#    2 -0.270109 -1.137184
#    3 -0.279335 -0.961327      -->Multi Index dataframe
# G2 1 -0.310862  0.532013
#    2  2.283137  1.274280
#    3  1.281153  1.630495
