import random
import string

def generate_password(length):
    lower_case = string.ascii_lowercase
    upper_case = string.ascii_uppercase
    digits = string.digits
    special_characters = string.punctuation
    all_characters = lower_case + upper_case + digits + special_characters
    length = max(length, 8)
    password = ''.join(random.choice(all_characters) for _ in range(length))
    
    return password

def main():
    length = int(input("Enter the desired length of the password: "))
    password = generate_password(length)
    print("Generated Password:", password)

if __name__ == "__main__":
    main()
