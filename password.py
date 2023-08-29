import random
import string
def generate_password(length):
    words = ["moon", "velvet", "garden", "crystal", "whisper", "serene", "ocean", "breeze", "enigma"]
    special_characters = "!@#$%^&*"
    password_length = max(8, length)  # Ensure a minimum length of 8
    word_length = password_length // 2
    digit_length = (password_length - word_length) // 2
    special_char_length = password_length - word_length - digit_length
    password = random.sample(words, word_length)
    password.extend(random.sample(string.digits, digit_length))
    password.extend(random.sample(special_characters, special_char_length))
    random.shuffle(password)
    generated_password = ''.join(password)
    return generated_password
if __name__ == "__main__":
    print("Welcome to Unique Password Generator!")
    try:
        password_length = int(input("Enter desired password length: "))
        if password_length < 1:
            raise ValueError
        generated_password = generate_password(password_length)
        print(f"Generated Password: {generated_password}")
    except ValueError:
        print("Invalid input. Please enter a valid password length.")
