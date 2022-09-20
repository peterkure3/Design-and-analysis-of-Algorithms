# Implementation of insertion sort
# Array z = [5,2,4,6,1,3]

z = [5,2,4,6,1,3]
x=1

print("Array z before sorting:")
print(z)

print("Size of array Z:")
print(len(z))

while x < len(z):
    c = z[x]
    y = x-1
    while y >=0 and z[y] > c:
        z[y+1] = z[y]
        y=y-1
    z[y+1] = c
    x=x+1

print("Array z after sorting:")
print(z)