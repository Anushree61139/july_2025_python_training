user_input=input("enter the text")
from datetime import datetime
current_datetime=datetime.now()
filename=str(current_datetime).replace(":","_")
with open(filename+".txt","w") as file:
    file.write(user_input)
print("your input has been saved to 'user_input.txt'")
