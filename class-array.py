# List for the mumbled data
mumbled_data = [["KATUKUNDA Rochelle","A94169","S21B23/016"],
["NAJJOBA Tracy","A95681","S21B23/034"],
["MUGANGA Charles","A96447","J22B23/032"],
["NKATA Joshua Luyombya","A94161","S21B23/008"],
["MUKISA Isaiah","A94160","S21B23/007"],["Afghanistan",93],
["Bahamas","1-242"],["Saint Vincent and the Grenadines","1-784"],["Tanzania",255],["Tiji",679],
["Ukraine",380]]

# Simple lineaer search algorithm

def linear_search(list,item):
# Loops through all the sub-lists in the list
    for i in list:
        #Loops through all items in each sub-lists
        for j in i:
            if item == j:
                return i
                
    return "Item not found!"                   
# linear_search(mumbled_data,item)

#Printing the results for the item search
print(linear_search(mumbled_data,7))
print(linear_search(mumbled_data,"A94160"))
print(linear_search(mumbled_data,380))
print(linear_search(mumbled_data,"Doe"))
