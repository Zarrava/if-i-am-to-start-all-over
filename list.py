holder = ["Sweden", "Denmark", "Us", "UK", "Nigeria"]
user_input = input("Guess the country: ").title().strip()
success_msg = f"Fantastic, {user_input} is correct"
failed_msg = f"Ehya, {user_input} is incorrect, Try again."

if user_input == holder[0]:
   print (success_msg)
elif user_input == holder[1]:
    print (success_msg)
elif user_input == holder[2]:
    print (success_msg)
elif user_input == holder[3]:
    print (success_msg)
elif user_input == holder [4]:
    print(success_msg)
else:
    print(failed_msg)