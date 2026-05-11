import secrets
import string

def generate_password(length: int) -> str:

    if length < 4:
        raise ValueError(
            "Password length must be at least 4."
        )

    # Character sets
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    special = string.punctuation

    # Combine all characters
    all_chars = (
        lowercase +
        uppercase +
        digits +
        special
    )

    # Ensure at least one character from each set
    password = [
        secrets.choice(lowercase),
        secrets.choice(uppercase),
        secrets.choice(digits),
        secrets.choice(special)
    ]

    # Fill remaining characters
    password.extend(
        secrets.choice(all_chars)
        for _ in range(length - 4)
    )

    # Shuffle password
    secrets.SystemRandom().shuffle(password)

    return ''.join(password)


def main():

    length = int(input(
        "Enter password length: "
    ))

    password = generate_password(length)

    print("Generated Password:", password)


if __name__ == "__main__":
    main()