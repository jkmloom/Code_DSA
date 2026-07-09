# Array (using numpy)

from numpy import *

# creating an array (using numpy)
# type code is optional in numpy
arr = array([1, 2, 3, 4, 5, 6, 7, 8, 9, 0])
arr2 = array([1, 2, 3, 4, 5, 6, 7, 8, 9, 0], float)

print("Array 1:")
# auto type-code
for x in arr:
    print(x, end=" | ")

print("\nArray 2:")
# manual type-code
for y in arr2:
    print(y, end=" | ")
print()

# numpy allows heterogeneuos elements in an array
array_var = array([1, 2.3, '4.5'])
print("Array 3: ", array_var, type(array_var))

# linspace-> range of numbers equally spaced
# syntax-> linspace(start, stop, no. of parts)
var = linspace(10, 20, 11)

print("Array 4:")
for z in var:
    print(z, end=" | ")
print()

# arange-> similar to linspace() but here spacing <-> distance to the next element
# syntax-> arange(start, stop, next_element_distance)
var2 = arange(10, 20, 2)

print("Array 5:")
for i in var2:
    print(i, end=" | ")
print()

# zeros & ones-> used for creating array of 0s and 1s
var3 = zeros(10)
var4 = ones(10)

print("Array 6:")
for j in var3:
    print(j, end=" | ")

print("\nArray 7:")
for k in var4:
    print(k, end=" | ")
print()

# full-> creating array of single value
# syntax-> full(no. of values, value)
var5 = full(10, 5)

print("Array 8:")
for l in var5:
    print(l, end=" | ")
print()