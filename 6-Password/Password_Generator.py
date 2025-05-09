import secrets
import string
import random

def generate_password(length=12, use_special_chars=True):
    if use_special_chars:
        characters = string.ascii_letters + string.digits + string.punctuation
    else:
        characters = string.ascii_letters + string.digits

    return ''.join(secrets.choice(characters) for _ in range(length))       

def generate_passwords(num_passwords=3, length=12, use_special_chars=True):
    return [generate_password(length, use_special_chars) for _ in range(num_passwords)] 

if __name__ == "__main__":
    try:
        length = int(input("Enter the desired password length: "))
        passwords = generate_passwords(length=length)
        print("Generated Passwords:")
        for password in passwords:
            print(password)

    except ValueError:
        print("Invalid input. Please enter a valid number.")