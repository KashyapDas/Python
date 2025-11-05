def linearSearch(arr,target) :
    for elem in arr :
        if(elem == target) : return arr.index(elem)
    
    return -1    

arr = []

arr_size = int(input("Enter the size of the array : "))
for index in range(0,arr_size,1):
    element = int(input(f"Enter the {index} element : "))
    arr.append(element)
target = int(input("Enter the target : "))

result = linearSearch(arr,target)
if result<0 :
    print("Element are not present...")
else : 
    print(f"Element are present at the index : {result}")
