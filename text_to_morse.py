import os

logo = """
  __  __                    ___         _        ___                     _           
 |  \/  |___ _ _ ___ ___   / __|___  __| |___   / __|___ _ ___ _____ _ _| |_ ___ _ _ 
 | |\/| / _ \ '_(_-</ -_) | (__/ _ \/ _` / -_) | (__/ _ \ ' \ V / -_) '_|  _/ -_) '_|
 |_|  |_\___/_| /__/\___|  \___\___/\__,_\___|  \___\___/_||_\_/\___|_|  \__\___|_|  
                                                                                     
"""

# Store morse conversions as dictionary
morse_dict = {'a': '.-', 'b': '-...', 'c': '-.-.', 'd': '-..', 'e': '.', 'f': '..-.', 'g': '--.', 'h': '....', 'i': '..',
              'j': '.---', 'k': '-.-', 'l': '.-..', 'm': '--', 'n': '-.', 'o': '---', 'p': '.--.', 'q': '..-.',
              'r': '.-.', 's': '...', 't': '-', 'u': '..-', 'v': '...-', 'x': '.--', 'y': '-.--', 'z': '--..',
              '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...',
              '8': '---..', '9': '----.', '0': '-----'}

# Loop to perform multiple conversions
run_converter = True
while run_converter:
    print(logo)
    print('Welcome to the Morse Code Converter!')
    # Ask for string to work on
    user_request = input(f'What would you like to convert?\n> ').lower()

    # Empty string to build converted string
    converted = ''

    # Iterate through characters in string and replace with appropriate conversion
    for char in user_request:
        # If space in string, replace space with /
        if char == ' ':
            converted += '/'
        else:
            converted += morse_dict[char]
    print(f'Here is your conversion!\n{converted}\n')
    
    # Ask for another conversion
    new_conversion = input('Would you like to convert another message? Please enter Yes or No.\n> ').lower()
    if new_conversion == 'no':
        # End loop
        run_converter = False
    else:
        os.system('cls')
