# Array in Python
# ***************
# Collection of similar types of elements (in languages like C and C++)
# Contiguous Memeory Allocation (in almost all the programming languages)
# In python: elements can be homo or hetero
# In C: int a[10];
# In Pyhton:: 1. Python Array Module
#             2. Python Numpy Module
# In Python array has dynamic memory allocation

from array import *

# syntax-> variable_name = array('type_code', [a, r, r, a, y])
val = array('i', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
val2 = array('u', ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j'])

print("Array 1: ")
for i in range(len(val)):
    print(val[i], end=' | ')
print()
# Inhanced for loop-> this method can also be used for printing the array
print("Array 2:")
for j in val:
    print(j, end=' | ')
print()

print("Array 3:")
for k in range((len(val2))):
    print(val2[k], end=" | ")
print()

# check array's type code
print(f"Type Code for Array 1: {val.typecode}")

print("Array 4:")
# Reverse the array
val.reverse()
for l in range(len(val)):
    print(val[l], end=' | ')
print()

# inserting element in an array
# syntax-> variable_name.insert(index, value)
val.insert(1, 50)
print("Array 5:")
for m in range(len(val)):
    print(val[m], end=' | ')
print()

# inserting/appending an element at the end of an array
print("Array 6:")
val.append(100)
for n in range(len(val)):
    print(val[n], end=' | ')
print()

# creating new array with the elements of an old array
print("Array 7:: Method 1:")
copy_array = array(val.typecode, val)
for o in range(len(copy_array)):
    print(copy_array[o], end=' | ')
print()
# another method
print("Array 7:: Method 2:")
copy_array2 = array(val.typecode, (p*2 for p in val))
for q in range(len(copy_array2)):
    print(copy_array2[q], end=' | ')
print()

# delete an element of an array (using index value)
print("Array 8:")
# syntax-> variable_name.pop(index_value)
copy_array2.pop(3)
for r in range(len(copy_array2)):
    print(copy_array2[r], end=' | ')
print()
# NOTE-> if no index value is passed in .pop() the last element is deleted

# delete an element of an array (passing the value itself)
copy_array2.remove(100)
print("Array 9:")
for s in range(len(copy_array2)):
    print(copy_array2[s], end=' | ')
print()

# slicing of an array (in python)
print("***"*20)
# syntax-> variable_name = array_variable[start_index:end_index]
abc = val[2:5]
print(f"Array 10: {abc}")

# slicing of an array (excluding some index values from last)
abc2 = val[2:-3]
print(f"Array 12: {abc2}")

# reverse array elements (through slicing)
abc_rev = abc2[::-1]
print(f"Array 12: {abc_rev}")
print("***"*20)
