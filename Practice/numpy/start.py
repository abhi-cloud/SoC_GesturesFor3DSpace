import numpy as np
import array

# l = list(range(10))
# a = array.array('i', l)
# print (l)
# print (a)

l1 = np.array([3.14, 3, 3, 4], dtype='int')

l2 = np.array([range(i, i+3) for i in [1, 2, 3]])

print (l2)