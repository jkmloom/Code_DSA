# Multi-dimentional array (using numpy)

from numpy import *

# 0-d array
zero_dimentional = array(10)
print("Zero Dimentional Array: ", zero_dimentional)

# 1-d array
one_dimentional = array([1, 2, 3, 4, 5])
print("One Dimentional Array: ", one_dimentional)

# 2-d array
two_dimentional = array([ [1, 2, 3], [4, 5, 6], [7, 8, 9] ])
print("Two Dimentional Array:\n", two_dimentional)

# 3-d array
three_dimentional = array([ [[1, 2], [3, 4]],
                           [[5, 6], [7, 8]] ])
print("Three Dimentional Array:\n", three_dimentional)