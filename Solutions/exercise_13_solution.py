person_name = "|\t \n elliott     |" #input stored in a variable/

print (f"This is the raw format: {person_name} \n") #variable displayed to the screen in raw format

#variable displays to screen in left, right and full strip respectively
print (f"This is the Left stripped version: {person_name.title().lstrip()}\n")
print (f"This is the right stripped version: {person_name.title().rstrip()}\n")
print (f"This is the Full stripped version: {person_name.title().strip()}\n")
