#this is to create a list called names
names = ["aderonke", "adekunle", "zeena", "eri", "ara", "elliott", "diva"]

symb = "undefined" #this variable will be used to hold names so that we can carryout slice operations init

#gets the user to input their first name
user_name = input("Kindly enter your name: ").strip().lower()

#now this section takes the user input and compare it with the names in the list
#then returns a personalized message.

if user_name == names[0]:
    symb = names[0]                 #this stores the name in the list into a new variable
    print(f"{symb[0].upper()} for {names[0].title()}") #this slices and return the first abbrieviation and the name back to the screen
elif user_name == names[1]:
    symb = names[1]
    print(f"{symb[0].upper()} for {names[1].title()}")
elif user_name == names[2]:
    symb = names[2]
    print(f"{symb[0].upper()} for {names[2].title()}")
elif user_name == names[3]:
    symb = names[3]
    print(f"{symb[0].upper()} for {names[3].title()}")
elif user_name == names[4]:
    symb == names[4] 
    print(f"{symb[0].upper()} for {names[4].title()}")
elif user_name == names[5]:
    symb == names[5] 
    print(f"{symb[0].upper()} for {names[5].title()}")
elif user_name == names[6]:
    symb == names[6]
    print(f"{symb[0].upper()} for {names[6].title()}")
else:
    print (f"{user_name[0].upper()} for {user_name.title()}")
    
    