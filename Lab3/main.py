def prepare_input(text):
    text = text.replace(" ", "").upper()
    text = text.replace("J", "I")
    return text

def find_char_coordinates(matrix, char):
    for row in range(5):
        for col in range(6):
            if matrix[row][col] == char:
                return row, col
    return find_char_coordinates(matrix, 'X')

def build_playfair_matrix(key):
    key = prepare_input(key)
    matrix = [['' for _ in range(6)] for _ in range(5)]
    key_chars = []
    for char in key:
        if char not in key_chars:
            key_chars.append(char)
    romanian_alphabet = "AĂÂBCDEFGHIÎKLMNOPQRSȘTȚUVWXYZ"
    index = 0
    for row in range(5):
        for col in range(6):
            if index < len(key_chars):
                matrix[row][col] = key_chars[index]
                romanian_alphabet = romanian_alphabet.replace(key_chars[index], "")
                index += 1
            else:
                matrix[row][col] = romanian_alphabet[0]
                romanian_alphabet = romanian_alphabet[1:]
    return matrix

def encrypt_playfair(plaintext, key):
    matrix = build_playfair_matrix(key)
    plaintext = prepare_input(plaintext)
    ciphertext = ""
    i = 0
    while i < len(plaintext):
        char1 = plaintext[i]
        char2 = ''
        if i + 1 < len(plaintext):
            char2 = plaintext[i + 1]
        if char1 == char2:
            char2 = 'X'
            i -= 1
        row1, col1 = find_char_coordinates(matrix, char1)
        row2, col2 = find_char_coordinates(matrix, char2)
        if row1 == row2:
            ciphertext += matrix[row1][(col1 + 1) % 6] + matrix[row2][(col2 + 1) % 6]
        elif col1 == col2:
            ciphertext += matrix[(row1 + 1) % 5][col1] + matrix[(row2 + 1) % 5][col2]
        else:
            ciphertext += matrix[row1][col2] + matrix[row2][col1]
        i += 2
    return ciphertext

def decrypt_playfair(ciphertext, key):
    matrix = build_playfair_matrix(key)
    decrypted_text = ""
    i = 0
    while i < len(ciphertext):
        char1 = ciphertext[i]
        char2 = ciphertext[i + 1]
        row1, col1 = find_char_coordinates(matrix, char1)
        row2, col2 = find_char_coordinates(matrix, char2)
        if row1 == row2:
            decrypted_text += matrix[row1][(col1 - 1) % 6] + matrix[row2][(col2 - 1) % 6]
        elif col1 == col2:
            decrypted_text += matrix[(row1 - 1) % 5][col1] + matrix[(row2 - 1) % 5][col2]
        else:
            decrypted_text += matrix[row1][col2] + matrix[row2][col1]
        i += 2
    return decrypted_text

def is_valid_keyword(keyword):
    romanian_alphabet = "AĂÂBCDEFGHIÎKLMNOPQRSȘTȚUVWXYZ"
    return all(char.upper() in romanian_alphabet for char in keyword) and len(keyword) >= 7

def main():
    while True:
        print("1. Encrypt")
        print("2. Decrypt")
        print("3. Quit")
        choice = input("Enter your choice: ")
        if choice == "1":
            key = input("Enter the keyword (min 7 characters, Romanian alphabet only): ")
            if not is_valid_keyword(key):
                print("Invalid keyword. Please use at least 7 characters from the Romanian alphabet.")
                continue
            plaintext = input("Enter the message to encrypt: ")
            encrypted_text = encrypt_playfair(plaintext, key)
            print("Encrypted:", encrypted_text)
        elif choice == "2":
            key = input("Enter the keyword (min 7 characters, Romanian alphabet only): ")
            if not is_valid_keyword(key):
                print("Invalid keyword. Please use at least 7 characters from the Romanian alphabet.")
                continue
            ciphertext = input("Enter the message to decrypt: ")
            decrypted_text = decrypt_playfair(ciphertext, key)
            print("Decrypted:", decrypted_text)
        elif choice == "3":
            break
        else:
            print("Invalid choice. Please select 1, 2, or 3.")

if __name__ == "__main__":
    main()
