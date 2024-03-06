import random
import string

def generate_password(length=12):
    # Define characters pool
    lowercase_letters = string.ascii_lowercase
    uppercase_letters = string.ascii_uppercase
    digits = string.digits
    special_characters = string.punctuation

    # Combine all characters
    all_characters = lowercase_letters + uppercase_letters + digits + special_characters

    # Generate password
    password = ''.join(random.choice(all_characters) for _ in range(length))
    return password

def main():
    print("Welcome to the Password Generator!")

    # Get user input for password length
    while True:
        try:
            length = int(input("Enter the length of the password (minimum 8 characters recommended): "))
            if length < 8:
                print("Password length should be at least 8 characters.")
            else:
                break
        except ValueError:
            print("Please enter a valid integer.")

    # Get user input for number of passwords to generate
    while True:
        try:
            num_passwords = int(input("Enter the number of passwords to generate: "))
            if num_passwords <= 0:
                print("Please enter a positive integer.")
            else:
                break
        except ValueError:
            print("Please enter a valid integer.")

    # Generate and print passwords
    print("\nGenerated Passwords:")
    for _ in range(num_passwords):
        password = generate_password(length)
        print(password)

if __name__ == "__main__":
    main()
