#this is to create a list called names
names = ["aderonke", "adekunle", "zeena", "eri", "ara", "elliott", "diva"]

#gets the user to input their first name
user_name = input("Kindly enter your name: ").strip().lower()

#now this section takes the user input and compare it with the names in the list
#then returns a personalized message.

if user_name == names[0]:
    print(f"You are welcome {names[0].title()}")
elif user_name == names[1]:
    print(f"You are welcome {names[1].title()}")
elif user_name == names[2]:
    print(f"You are welcome {names[2].title()}")
elif user_name == names[3]:
    print(f"You are welcome {names[3].title()}")
elif user_name == names[4]:
    print(f"You are welcome {names[4].title()}")
elif user_name == names[5]:
    print(f"You are welcome {names[5].title()}")
elif user_name == names[6]:
    print(f"You are welcome {names[6].title()}")
else:
    print (f"You are not welcome here {user_name.title()}")
    
    