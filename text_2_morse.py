from ascii_art import logo
from encoding import ENCODERS


print(logo)

user_input = input('Enter text: \n').lower()
user_list = [letter for letter in user_input]
morse_code_list = [ENCODERS[letter] for letter in user_list]
morse_code = ' '.join(morse_code_list)

print(morse_code)
