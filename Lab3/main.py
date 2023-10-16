import random
import re


def find_letter_indices(letter, matrix):
    for row_index, row in enumerate(matrix):
        for col_index, value in enumerate(row):
            if value == letter:
                return row_index, col_index
    # If the letter is not found, return None or another appropriate value
    return None


def romanian_language(string):
    romanian_pattern = r'^[a-zA-ZăĂâÂșȘțȚîÎ]+$'
    if re.match(romanian_pattern, string):
        return True
    else:
        print(
            "Error: The string should only contain characters from the Romanian alphabet (A-Z, a-z, and special Romanian characters).")
        return False


def add_letters(message):
    # Characters to insert when two identical characters are adjacent
    insertion_characters = ['Q', 'X', 'Z']
    message_list = list(message)  # Convert the message to a list for easier manipulation
    i = 0
    while i < len(message_list) - 1:
        if message_list[i] == message_list[i + 1]:
            # Insert a random character from the insertion list
            message_list.insert(i + 1, random.choice(insertion_characters))
        i += 2
    # If the message has an odd length, add additional letter
    if len(message_list) % 2 != 0:
        message_list.append('F')
    # Convert the list back to a string
    return "".join(message_list)


def encrypt(message, matrix):
    message = list(message)  # Convert the message to a list
    for i in range(0, len(message), 2):
        letter1, letter2 = message[i], message[i + 1]
        row1, column1 = find_letter_indices(letter1, matrix)
        row2, column2 = find_letter_indices(letter2, matrix)
        # Implement first condition.
        if row1 != row2 and column1 != column2:
            message[i] = matrix[row1][column2]
            message[i + 1] = matrix[row2][column1]
        # Implement second condition.
        elif row1 == row2:
            columns = len(matrix[0])
            next_column1 = (column1 + 1) % columns
            next_column2 = (column2 + 1) % columns
            message[i] = matrix[row1][next_column1]
            message[i + 1] = matrix[row2][next_column2]
        # Implement third condition.
        elif column1 == column2:
            rows = len(matrix)
            next_row1 = (row1 + 1) % rows
            next_row2 = (row2 + 1) % rows
            message[i] = matrix[next_row1][column1]
            message[i + 1] = matrix[next_row2][column2]
    return "".join(message)  # Convert the list back to a string


def decrypt(ciphertext, matrix):
    ciphertext = list(ciphertext)  # Convert the ciphertext to a list
    for i in range(0, len(ciphertext), 2):
        letter1, letter2 = ciphertext[i], ciphertext[i + 1]
        row1, column1 = find_letter_indices(letter1, matrix)
        row2, column2 = find_letter_indices(letter2, matrix)
        # Implement first condition.
        if row1 != row2 and column1 != column2:
            ciphertext[i] = matrix[row1][column2]
            ciphertext[i + 1] = matrix[row2][column1]
        # Implement second condition.
        elif row1 == row2:
            columns = len(matrix[0])
            next_column1 = (column1 - 1) % columns
            next_column2 = (column2 - 1) % columns
            ciphertext[i] = matrix[row1][next_column1]
            ciphertext[i + 1] = matrix[row2][next_column2]
        # Implement third condition.
        elif column1 == column2:
            rows = len(matrix)
            next_row1 = (row1 - 1) % rows
            next_row2 = (row2 - 1) % rows
            ciphertext[i] = matrix[next_row1][column1]
            ciphertext[i + 1] = matrix[next_row2][column2]
    # Eliminate the added Q, X, or Z
    i = 0
    while i < len(ciphertext) - 2:
        if ciphertext[i] == ciphertext[i + 2] and ciphertext[i + 1] in ['Q', 'X', 'Z']:
            del ciphertext[i + 1]
            i += 1
        else:
            i += 2
    # Eliminate the last letter added
    if ciphertext[-1] == "F":
        ciphertext.pop()
    return "".join(ciphertext)  # Convert the list back to a string


def create_matrix(key):
    # Create the initial matrix with 5 rows and 6 columns
    matrix = [['' for _ in range(6)] for _ in range(5)]
    # Define the alphabet without J and duplicate letters
    alphabet = "AĂÂBCDEFGHIÎKLMNOPQRSȘTȚUVWXYZ"
    unique_key = ''.join(dict.fromkeys(key.upper()))  # Remove duplicates and make uppercase
    # Fill the matrix with unique characters from the key and then the remaining alphabet
    key_index = 0
    for row in range(5):
        for col in range(6):
            if key_index < len(unique_key):
                matrix[row][col] = unique_key[key_index]
                key_index += 1
            else:
                # Fill with remaining alphabet characters
                while alphabet and matrix[row][col] == '':
                    letter = alphabet[0]
                    alphabet = alphabet[1:]
                    # Skip the letter 'J' if it's in the alphabet
                    if letter != 'J':
                        matrix[row][col] = letter
    return matrix


def input_key():
    key = input("Key: ")
    key = key.replace(" ", "")
    while not (romanian_language(key) and len(key) >= 7):
        print(
            "Ensure that the characters are within the range 'A'-'Z' or 'a'-'z' (romanian lang.), and that the key is at least 7 characters long")
        key = input("Key: ")
        key = key.replace(" ", "")
    key = key.upper()
    key = key.replace("J", "I")
    key = ''.join(dict.fromkeys(key))  # Eliminate duplicates
    return key


if __name__ == "__main__":
    print('SELECT:')
    print('\t  \tE - Encryption \tD - Decryption \t Exit - Exit')

    while True:
        command = input("\nAction: ")
        if command == "E":
            message = input("Message: ")
            message = message.replace(" ", "")
            while not romanian_language(message):
                print("Characters have to be in the interval 'A'-'Z', 'a'-'z' corresponding to the Romanian language.")
                message = input("Message: ")
                message = message.replace(" ", "")
            message = message.upper()
            message = message.replace("J", "I")
            message = add_letters(message)
            key = input_key()
            matrix = create_matrix(key)
            ciphertext = encrypt(message, matrix)
            print("Ciphertext: " + ciphertext)

        elif command == "D":
            ciphertext = input("Ciphertext: ")
            ciphertext = ciphertext.upper()
            while not (romanian_language(ciphertext) and "J" not in ciphertext):
                print("Chars have to be in the interval 'A'-'Z', 'a'-'z'" " without 'J', 'j'")
                ciphertext = input("Ciphertext: ")
                ciphertext = ciphertext.upper()
            ciphertext = ciphertext.replace(" ", "")
            ciphertext = list(ciphertext)
            key = input_key()
            matrix = create_matrix(key)
            decrypted_message = decrypt(ciphertext, matrix)
            print("Message: " + decrypted_message)

        elif command == "Exit":
            break
