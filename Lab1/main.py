def caesar_cipher(text, key, operation):
    def encrypt_char(char, base, key):
        return chr((ord(char) - base + key) % 26 + base)

    def decrypt_char(char, base, key):
        return chr((ord(char) - base - key) % 26 + base)

    result = []

    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')

            if operation == 'encrypt':
                new_char = encrypt_char(char, base, key)
            elif operation == 'decrypt':
                new_char = decrypt_char(char, base, key)
            else:
                return "Invalid operation. Choose 'encrypt' or 'decrypt'."
            result.append(new_char)
        else:
            return "Invalid input. Only letters are permitted."

    return ''.join(result)

def print_shifted_alphabet(key, operation):
    if operation == 'encrypt':
        alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        shifted_alphabet = alphabet[key:] + alphabet[:key]
        print(f"Original Alphabet: {alphabet}")
        print(f"Shifted Alphabet (Key = {key}): {shifted_alphabet}")

def main():
    operations = ['encrypt', 'decrypt']

    while True:
        operation = input("Enter operation ('encrypt', 'decrypt', or 'exit' to quit): ").lower()

        if operation == 'exit':
            print("Done!")
            break  # Exit the loop and end the program

        if operation not in operations:
            print("Invalid operation. Only 'encrypt', 'decrypt', or 'exit'.")
            continue  # Continue to the next iteration

        key_input = input("Enter a key (1-25): ")
        if not key_input.isdigit():
            print("Invalid key. Please enter a numeric key.")
            continue  # Continue to the next iteration

        key = int(key_input)
        if not (1 <= key <= 25):
            print("Invalid key. Please select a key within the range of 1 to 25.")
            continue  # Continue to the next iteration

        text = input("Enter the message or cryptogram: ").replace(" ", "").upper()

        result = caesar_cipher(text, key, operation)
        print(f"Result: {result}")

        # Print the shifted alphabet for encryption
        print_shifted_alphabet(key, operation)

if __name__ == "__main__":
    main()
