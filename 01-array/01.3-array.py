from array import *

# searching an array
arr = array('i', [12, 45, 67, 54, 87, 50])

search_element = 54

if search_element in arr:
    i = arr.index(search_element)
    print(f"{search_element} was found at the index: {i}")
else:
    print(f"{search_element} element not present in the array!")