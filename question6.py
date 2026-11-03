try:
    num1=int(input("Enter First number:"))
    num2=int(input("Enter second number:"))
    result=num1/num2
except ZeroDivisionError:
    print("Cannot divide by Zero")
except ValueError:
    print("Invalid Input")