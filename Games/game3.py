def matchmaking_game():
    print("=" * 50)
    print("WELCOME TO THE NAME MATCHMAKING GAME!")
    print("=" * 50)
    print()
    
    # Get input from user
    male_name = input("Enter the male name: ").lower().replace(" ", "")
    female_name = input("Enter the female name: ").lower().replace(" ", "")
    
    # Convert names to lists for easier manipulation
    male_letters = list(male_name)
    female_letters = list(female_name)
    
    # Remove matching letters
    for letter in male_name:
        if letter in female_letters and letter in male_letters:
            male_letters.remove(letter)
            female_letters.remove(letter)
    
    # Count remaining letters
    remaining_count = len(male_letters) + len(female_letters)
    
    # Define relationship charts
    friends = [0, 3, 6, 9]
    marriage = [1, 4, 7, 10]
    enemies = [2, 5, 8, 11]
    
    # Determine relationship
    print()
    print("=" * 50)
    print(f"Remaining letters count: {remaining_count}")
    print()
    
    if remaining_count in friends:
        result = "FRIENDS"
    elif remaining_count in marriage:
        result = "MARRIAGE"
    elif remaining_count in enemies:
        result = "ENEMIES"
    else:
        # For counts beyond 11, use modulo to cycle through the pattern
        remainder = remaining_count % 12
        if remainder in friends:
            result = "FRIENDS"
        elif remainder in marriage:
            result = "MARRIAGE"
        else:
            result = "ENEMIES"
    
    print(f"Relationship Status: {result} ❤️" if result == "MARRIAGE" else f"Relationship Status: {result}")
    print("=" * 50)
    
    # Ask if user wants to play again
    print()
    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again in ['yes', 'y']:
        print()
        matchmaking_game()
    else:
        print("\nThanks for playing! Goodbye!")

# Run the game
if __name__ == "__main__":
    matchmaking_game()