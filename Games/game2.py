# Country guessing game
countries = ["Nigeria", "Kenya", "Ghana", "Egypt", "Morocco", "Tanzania", "Uganda", "Ethiopia"]

print("Welcome to the Country Guessing Game!")
print("\nHere are the countries to choose from:")
for country in countries:
    print(f"  - {country}")

secret_country = "Nigeria"
tries = 0

print("\nNow, try to guess which country I'm thinking of!")

while True:
    user_guess = input("Enter your guess: ").strip()
    tries += 1
    
    if user_guess.lower() == secret_country.lower():
        print(f"\nCongratulations! You guessed it correctly!")
        print(f"It took you {tries} {'try' if tries == 1 else 'tries'} to get the answer.")
        break
    else:
        print("Sorry, that's not correct. Try again!")