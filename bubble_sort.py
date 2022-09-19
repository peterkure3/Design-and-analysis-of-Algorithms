# bubble sort algorithm
# 31, 41,59, 26, 41,58
# desired order 26, 31, 41, 41,58, 59

def bubblesort(list):
    
# Swaps the elements to arrange them in  order
    for i in range(len(list)-1,0,-1):
        for idx in range(i):
            if list[idx]>list[idx+1]:
                temp = list[idx]
                list[idx]=list[idx+1]
                list[idx+1]=temp

list = [31,41,59,26,41,58]
bubblesort(list)
print(list)