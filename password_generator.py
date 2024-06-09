import random
import string

def generate_password(length, complexity):
    if complexity == "less":
        characters = string.ascii_letters + string.digits
    elif complexity == "moderate":
        characters = string.ascii_letters + string.digits + string.punctuation
    elif complexity == "high":
        characters = string.ascii_letters + string.digits + string.punctuation + string.ascii_uppercase + string.ascii_lowercase
    else:
        return "Invalid complexity level"

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    length = int(input("Enter the length of the password: "))
    complexity = input("Enter the complexity level (less, moderate, high): ").lower()
    
    password = generate_password(length, complexity)
    print("Your password:", password)

if __name__ == "__main__":
    main()
