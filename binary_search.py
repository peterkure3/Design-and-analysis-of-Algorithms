# Binary search algorithm
# given array [31,41,59,26,41,58]
# desired element 55

def binary_search(arr, down, up, x):
 
    
    if up >= down:
 
        mid = (up + down) // 2
 
        # If element is present at the middle itself
        if arr[mid] == x:
            return mid
 
        # Else element is at left subarray
        elif arr[mid] > x:
            return binary_search(arr, down, mid - 1, x)
 
        # The element can only be at the right subarray
        else:
            return binary_search(arr, mid + 1, up, x)
 
    else:
        # Element is absent in the array
        return -1
 
# Given array
arr = [31,41,59,26,41,58]
x = 55
 
# calling the function
result = binary_search(arr, 0, len(arr)-1, x)

# element is present in the array
if result != -1:
    print("True")
    
# element is absent in the array
else:
    print("False")