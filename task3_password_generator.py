# ============================================================
# TASK 3 - PASSWORD GENERATOR
# CodSoft Python Programming Internship
# ============================================================

import random
import string

def generate_password(length, use_upper=True, use_digits=True, use_symbols=True):
    """Generate a random password based on user preferences."""
    characters = string.ascii_lowercase  # always include lowercase

    if use_upper:
        characters += string.ascii_uppercase
    if use_digits:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation

    if not characters:
        characters = string.ascii_lowercase

    # Guarantee at least one character from each selected category
    password = []
    if use_upper:
        password.append(random.choice(string.ascii_uppercase))
    if use_digits:
        password.append(random.choice(string.digits))
    if use_symbols:
        password.append(random.choice(string.punctuation))
    password.append(random.choice(string.ascii_lowercase))

    # Fill the rest randomly
    remaining = length - len(password)
    password += random.choices(characters, k=remaining)

    # Shuffle so guaranteed chars aren't always at the front
    random.shuffle(password)
    return "".join(password)

def check_strength(password):
    """Evaluate and return password strength."""
    score = 0
    feedback = []

    if len(password) >= 8:
        score += 1
    if len(password) >= 12:
        score += 1
    if any(c.isupper() for c in password):
        score += 1
    if any(c.isdigit() for c in password):
        score += 1
    if any(c in string.punctuation for c in password):
        score += 1

    if score <= 2:
        return "🔴 Weak"
    elif score <= 3:
        return "🟡 Moderate"
    elif score == 4:
        return "🟢 Strong"
    else:
        return "🔵 Very Strong"

def get_yes_no(prompt):
    while True:
        ans = input(prompt).strip().lower()
        if ans in ("yes", "y"):
            return True
        elif ans in ("no", "n"):
            return False
        print("  Please enter yes or no.")

def main():
    print("\n" + "=" * 45)
    print("       🔐  PASSWORD GENERATOR")
    print("=" * 45)

    while True:
        print()

        # Get desired length
        while True:
            try:
                length = int(input("  Enter desired password length (4-64): "))
                if 4 <= length <= 64:
                    break
                print("  ⚠️  Please enter a length between 4 and 64.")
            except ValueError:
                print("  ⚠️  Invalid input! Enter a whole number.")

        # Get complexity preferences
        print("\n  Customize your password (press Enter for yes):")
        use_upper   = get_yes_no("  Include uppercase letters? (yes/no): ")
        use_digits  = get_yes_no("  Include digits (0-9)?       (yes/no): ")
        use_symbols = get_yes_no("  Include symbols (!@#...)?   (yes/no): ")

        # Generate & display
        password = generate_password(length, use_upper, use_digits, use_symbols)
        strength = check_strength(password)

        print("\n" + "=" * 45)
        print(f"  Generated Password : {password}")
        print(f"  Password Length    : {len(password)}")
        print(f"  Strength           : {strength}")
        print("=" * 45)

        # Option to generate another
        again = get_yes_no("\n  Generate another password? (yes/no): ")
        if not again:
            print("\n  🔒 Keep your passwords safe! Goodbye!\n")
            break

if __name__ == "__main__":
    main()
