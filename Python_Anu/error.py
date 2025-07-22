num=input("Enter a number:")
try:
    if not num.isnumeric():
        raise ValueError("Input must be a numerical values:")

except ValueError as e:
    print(e)

    
        
