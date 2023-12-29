import random
import string

def generate_password(length):
    # Define the character sets for different complexity levels
    lower_case = string.ascii_lowercase
    upper_case = string.ascii_uppercase
    digits = string.digits
    special_characters = string.punctuation

    # Combine character sets based on complexity
    all_characters = lower_case + upper_case + digits + special_characters

    # Ensure length is at least 8 characters
    length = max(length, 8)

    # Generate a random password using the selected character sets
    password = ''.join(random.choice(all_characters) for _ in range(length))
    
    return password

def main():
    # Prompt the user for the desired length of the password
    length = int(input("Enter the desired length of the password: "))

    # Generate the password
    password = generate_password(length)

    # Display the generated password
    print("Generated Password:", password)

if __name__ == "__main__":
    main()
