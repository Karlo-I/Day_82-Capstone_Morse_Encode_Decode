# Define dictionaries to map letters and digits to Morse code and vice versa
TEXT_TO_MORSE_DICT = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....', 'I': '..',
    'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
    'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..',

    '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..',
    '9': '----.', '0': '-----',

    ',': '--..--', '.': '.-.-.-', '?': '..--..', '/': '-..-.', '-': '-....-', '(': '-.--.', ')': '-.--.-', ' ': '/'
}

MORSE_TO_TEXT_DICT = {
    ".-": "A", "-...": "B", "-.-.": "C", "-..": "D", ".": "E", "..-.": "F", "--.": "G", "....": "H", "..": "I",
    ".---": "J", "-.-": "K", ".-..": "L", "--": "M", "-.": "N", "---": "O", ".--.": "P", "--.-": "Q", ".-.": "R",
    "...": "S", "-": "T", "..-": "U", "...-": "V", ".--": "W", "-..-": "X", "-.--": "Y", "--..": "Z",

    "-----": "0", ".----": "1", "..---": "2", "...--": "3", "....-": "4", ".....": "5", "-....": "6", "--...": "7",
    "---..": "8", "----.": "9",

    '--..--': ',', '.-.-.-': '.', '..--..': '?', '-..-.': '/', '-....-': '-', '-.--.': '(', '-.--.-': ')', '/': ' '
}

# Function to convert text to Morse code
def text_to_morse(text):
    text = text.upper()  # Convert the text to uppercase
    morse_code = []

    for char in text:
        if char in TEXT_TO_MORSE_DICT:
            morse_code.append(TEXT_TO_MORSE_DICT[char])
        else:
            morse_code.append('?')  # In case a character is not found in the dictionary (e.g. special characters)

    # .join() method used to join elements of a iterable (list, tuple, or set) into a single string
    return ' '.join(morse_code)

# Function to convert Morse code to text
def morse_to_text(morse):
    decode_text = []
    morse_list = morse.split(" ")

    for char in morse_list:
        if char in MORSE_TO_TEXT_DICT:
            decode_text.append(MORSE_TO_TEXT_DICT[char])
        else:
            decode_text.append('?')  # In case a character is not found in the dictionary (e.g. special characters)

    # .join() method used to join elements of a iterable (list, tuple, or set) into a single string
    return ' '.join(text)

# Main program
program_on = True
while program_on:
    answer = input('Type "e" to encode, "d" to decode and "q" to quit:  ').lower()

    if answer == "e":
        text = input("Enter your text: ").upper()
        morse_code = text_to_morse(text)
        print(f"Morse code: {morse_code}")

    elif answer == "d":
        morse_codes = input("Enter your morse codes: ")
        plain_text = morse_to_text(morse_codes)
        print(f"Decoded text: {plain_text.lower().capitalize()}")

    elif answer == "q":
        program_on = False

    else:
        print("Invalid response. Please try again.")
