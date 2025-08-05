import random
import string

def generate_password(length):
    if length < 4:
        return "Password length should be at least 4 for strong security."

    # Define character pools
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    digits = string.digits
    symbols = string.punctuation

    # Ensure password has at least one character from each group
    password = [
        random.choice(lower),
        random.choice(upper),
        random.choice(digits),
        random.choice(symbols)
    ]

    # Fill the rest of the password length
    if length > 4:
        all_chars = lower + upper + digits + symbols
        password += random.choices(all_chars, k=length - 4)

    # Shuffle to prevent predictable sequences
    random.shuffle(password)

    return ''.join(password)

# Example usage
length = int(input("Enter desired password length: "))
print("Generated Password:", generate_password(length))
