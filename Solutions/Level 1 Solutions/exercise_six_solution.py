message = "   welcome to PYTHON programming   " #this variable is filled with lots of unwanted spacing

message = message.strip()  #this cleans the leading and trailing spaces and updates the variable.

print(f"Title case: {message.title()}") #this returns the title case to the screen
print(f"Uppercase: {message.upper()}") #this return the uppercase version of the message to the screen