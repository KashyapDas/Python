stringCheck = input("Enter a string you want to check : ")


def isPalindrom(stringCheck):
    start = 0;
    end = len(stringCheck)-1
    while start <= end :
        if stringCheck[start] != stringCheck[end] : return 0 
        start+=1
        end-=1
    return 1

isTrue = isPalindrom(stringCheck.upper())
if isTrue == 0 :
    print("Its not palindrome")
elif isTrue == 1 :
    print("Its palindrome")
else : 
    print("Invalid Input")