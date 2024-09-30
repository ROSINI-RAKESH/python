try:
    a=int(input("Enter the number:"))
    b=int(input("Enter the number:"))
    result=a+b
    print("The result is:",result)
except NameError:
    print("Variable is not defined")
except ValueError:
    print("The values should be in number not in words")
finally:
    print("Thank you for visiting this page")