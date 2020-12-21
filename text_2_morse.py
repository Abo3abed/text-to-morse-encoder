from ascii_art import logo
from encoding import ENCODERS


print(logo)
user_list = [letter for letter in (input('Enter text: \n').lower())] 
morse_code = ' '.join([ENCODERS[letter] for letter in user_list])
print(morse_code)
