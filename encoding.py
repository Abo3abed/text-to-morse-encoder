# -----------------------------Constants---------------------------------

ENCODERS = {
    'a': '.-',
    'b': '-...',
    'c': '-.-.',
    'd': '-..',
    'e': '.',
    'f': '..-.',
    'g': '--.',
    'h': '....',
    'i': '..',
    'j': '.---',
    'k': '-.-',
    'l': '.-..',
    'm': '--',
    'n': '-.',
    'o': '---',
    'p': '.--.',
    'q': '--.-',
    'r': '.-.',
    's': '...',
    't': '-',
    'u': '..-',
    'v': '...-',
    'w': '.--',
    'x': '-..-',
    'y': '-.--',
    'z': '--..',
    '1': '.----',
    '2': '..---',
    '3': '...--',
    '4': '....-',
    '5': '.....',
    '6': '-....',
    '7': '--...',
    '8': '---..',
    '9': '----.',
    '10': '-----'
}

# --------------------------Extra Feature-----------------------------

# checking for duplicate values in case mistakenly copied the encoding from the wiki list
# reversed_dict = {}
#
# for (key, value) in ENCODERS.items():
#     reversed_dict.setdefault(value, set()).add(key)
#
# check_duplicates = [key for (key, values) in reversed_dict.items() if len(values) > 1]
#
# print(check_duplicates)
# if the output is an empty list that means you have no duplicate values