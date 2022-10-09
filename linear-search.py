# Implementing linear serach
a=[11,423,172,32,910,9,21,45,172]
def linearsearch(a,value):
    for i in range(len(a)):
        if a[i] == value:
            return i
    return -1

print(linearsearch(a,172))

# worstcase
def conradsearch(a,value):
    z=[]
    for i in range(len(a)):
        if a[i] == value:
            z.append(i)
    return z

print(conradsearch(a,172))