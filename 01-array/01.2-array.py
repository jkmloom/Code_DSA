from array import *

# creating an array (on user input)
arr = array('i', [])

print("")
n = int(input("How many elements do you want in this array? "))

for i in range(1, n+1):
    arr.append(int(input("Enter next element: ")))

print(f"{"***"*10}\nFinal Array: ")
for x in arr:
    print(x, end=' ')
print()