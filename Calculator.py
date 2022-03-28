def addition(a,b):
    return a+b
def substraction(a,b):
    return a-b
def multiply(a,b):
    return a*b
def divide(a,b):
    return a/b

if __name__=="__main__":
    num1 = int(input("Enter the First number: "))
    num2 = int(input("Enter the Second number: "))
    result = addition(num1,num2)
    result1 = substraction(num1,num2)
    result2 = multiply(num1,num2)
    result3 = divide(num1,num2)
    print(result)
    print(result1)
    print(result2)
    print(result3)