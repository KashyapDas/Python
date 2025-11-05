def BinarySearch(arr,target):
    start = 0
    end = len(arr)-1
    mid = int((start+end)/2)
    while start<=end:
        if arr[mid] == target : return mid
        elif arr[mid] < target : start = mid +1
        else : end = mid -1 
        mid = int((start+end)/2)
    return -1

arr = []

size = int(input("Enter the size : "))

for index in range(0,size,1) :
    arr.append(int(input(f"Enter the {index} element : "))) 

target = int(input("Enter the target : "))

result = BinarySearch(arr,target)

if result < 0 :
    print("Element is not at any index of the array...")
else : 
    print(f"Element is found at the index : {result}")
