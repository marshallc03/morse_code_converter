import string

### CONSTANTS ###
ENG_TO_MORSE = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
                'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
                'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
                'Y': '-.--', 'Z': '--..', '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
                '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.', ' ': '/'}

original_string = input("Enter text to convert to Morse Code: ")

new_string = original_string.translate(str.maketrans('', '', string.punctuation)).upper()

print(new_string)

morse_code = ""

for char in new_string:
    morse_code += ENG_TO_MORSE.get(char)
    morse_code += " "

print(morse_code)
