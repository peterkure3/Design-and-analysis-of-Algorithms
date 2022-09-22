
def merge_sort(a,b):
    sorted_array=[]
    x=0
    y=0
    len_a = len(a)
    len_b = len(b)

    while x < len_a and y < len_b:
        if a[x] <= b[y]:
            sorted_array.append(a[x])
            x+=1
        else:
            sorted_array.append(b[y])
            y+=1

    while x < len_a:
        sorted_array.append(a[x])
        x+=1
    while y < len_b:
        sorted_array.append(b[y])
        y+=1
    return sorted_array

A=[2,100,1000]
B=[1,699,1000000,1000001]
print(merge_sort(A, B))