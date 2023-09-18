# Function to generate a new alphabet based on key2
def generate_new_alphabet(key2):
    # Sort and remove duplicates from key2, convert to uppercase
    key2 = ''.join(sorted(set(key2.upper()), key=key2.upper().index))

    # Generate the original alphabet (A-Z)
    alphabet = ''.join(chr(ord('A') + i) for i in range(26))

    # Create a new alphabet by adding key2 and removing its characters from the original alphabet
    new_alphabet = key2 + ''.join(char for char in alphabet if char not in key2)

    print(f'New Alphabet: {new_alphabet}')

    return new_alphabet

# Function to perform Caesar cipher encryption/decryption
def caesar_cipher(input_text, key1, key2, operation):
    # Generate the new alphabet
    new_alphabet = generate_new_alphabet(key2)

    # Check if key1 is within the valid range
    if not (1 <= key1 <= 25):
        return 'Invalid key. Key must be between 1 and 25.'

    # Convert input text to uppercase and remove spaces
    modified_text = ''.join(input_text.split()).upper()
    result = ''

    for char in modified_text:
        if char in new_alphabet:
            index = new_alphabet.index(char)
            if operation == 'encrypt':
                new_index = (index + key1) % len(new_alphabet)
            elif operation == 'decrypt':
                new_index = (index - key1 + len(new_alphabet)) % len(new_alphabet)
            else:
                return 'Invalid operation. Operation must be encrypt, decrypt, or exit.'
            result += new_alphabet[new_index]
        else:
            return 'Invalid character. Only alphabet characters (A-Z) are allowed.'

    return result

# Main program loop
while True:
    operation = input(
        'Select operation (encrypt, decrypt, or exit to quit): ').strip().lower()

    if operation == 'exit':
        print('Exiting the program. Goodbye!')
        break
    elif operation not in ('encrypt', 'decrypt'):
        print('Invalid operation. Please enter encrypt, decrypt, or exit to quit.')
        continue

    key1_input = input('Enter the first key (Integer value between 1-25): ').strip()

    try:
        key1 = int(key1_input)
        if not (1 <= key1 <= 25):
            print('Invalid key. Key must be between 1 and 25.')
            continue
    except ValueError:
        print('Invalid key. Key must be an integer between 1 and 25.')
        continue

    key2 = input(
        'Enter the second key (minimum 7 characters. ): ').strip()

    if len(key2) < 7:
        print('Invalid key. Second key must be at least 7 characters long.')
        continue

    message = input('Enter message: ')
    result = caesar_cipher(message, key1, key2, operation)
    print(f'Result: {result}')
