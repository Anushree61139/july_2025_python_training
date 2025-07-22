user_input=input("Enter some text to save the file")
with open("user_input.txt","w")as file:
    file.write(user_input)
print("your input has been saved in user_input.txt")
