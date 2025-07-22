num1 = input("enter the first number:")
num2= input("enter the second number:")
action =input("enter the action")sssss
try:
    if not num1.isnumeric() or not num2.isnumeric():
        raise ValueError("input must br numerical valures:")
    num1=float(num1)
    