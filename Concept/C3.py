# Conditional Statement 
a = int(input("Enter an input : "))

if a<0 :
    print("Number is negative")
elif a>0 :
    print("Number is positive")
else : 
    print("Number is 0")
    

# Range Function
number = int(input("Enter a number : "))
for elem in range(1,number+1,1) :
    print(elem,end=" ")

print()
# Looping 
arr = [10,20,30,40,50]
# for loop
for i in arr:
    print(i,end=" ")

print()
# while loop 
index = 0;
while index<len(arr) :
    print("While loop",end=" ")
    index=index+1

