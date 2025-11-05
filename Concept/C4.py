# Functions are created using the def keyword

def printText() :
    print("Hello World")

def sumNumber(number1, number2):
    return (number1+number2)

number1 = int(input("Enter number 1 : "))
number2 = int(input("Enter number 2 : "))

printText()

result = sumNumber(number1,number2)
print("Sum of 2 number is",result,end="")