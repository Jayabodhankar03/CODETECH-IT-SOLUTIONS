import random
import string

def generate_password(length, complexity):
    if complexity == 'low':
        characters = string.ascii_letters + string.digits
    elif complexity == 'medium':
        characters = string.ascii_letters + string.digits + string.punctuation
    elif complexity == 'high':
        characters = string.ascii_letters + string.digits + string.punctuation + string.ascii_uppercase + string.ascii_lowercase
    else:
        print("Invalid complexity level. Please choose from 'low', 'medium', or 'high'.")
        return None

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    length = int(input("Enter the desired length of the password: "))
    complexity = input("Enter the desired complexity level (low/medium/high): ").lower()

    password = generate_password(length, complexity)
    if password:
        print("Generated password:", password)

if __name__ == "__main__":
    main()
