# Simple guessing game
countries = ["germany", "canada", "nigeria", "UK", "US", "sweden", "crotia", "mexico", "ghana", "senegal" ]
secret_word = countries[1]
entries = 0

print(f"{countries}")
print("Try to guess the countryz: ")

while True:
    user_guess = input("Enter your guess: ").lower().strip()
    
    if user_guess == secret_word:
        print(f"Congratulations! You guessed it correctly after {entries} attempts")
        break
    else:
        entries += 1
        print("Sorry, that's not correct. Try again!")
    