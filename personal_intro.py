# Project: Personal Introduction Program
# Description: A program that asks for user details and displays a formatted welcome message.

def main():
    # 1. Get user input (Technical Requirement: Use input() and variables)
    # We add a space after the question mark for better readability in the terminal
    name = input("What is your name? ")
    age = input("How old are you? ")
    hobby = input("What is your favorite hobby? ")

    # 2. Display the friendly welcome message (Technical Requirement: Use print() and f-strings)
    # The output format matches the "Sample Output" screenshot with emojis
    print(f"\n🎉 Welcome {name}! 🎉")
    print(f"You are {age} years old and love {hobby}.")

if __name__ == "__main__":
    main()
