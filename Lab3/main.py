import random
import re


def romanian_language(string):
    pattern = r'^[a-zA-ZăĂâÂșȘțȚîÎ]+$'
    return bool(re.match(pattern, string))


def add_letters(message):
    to_insert = ['Q', 'X', 'Z']
    message, i = list(message), 0
    while i < len(message) - 1:
        if message[i] == message[i + 1]:
            message.insert(i + 1, random.choice(to_insert))
        i += 2
    # Add additional letter to the end  if the message has an odd length
    if len(message) % 2 != 0:
        message.append('F')
    return message


def find_letter_indices(letter, matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == letter:
                return i, j


def encrypt(message, matrix):
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
    return "".join(message)


def decrypt(ciphertext, matrix):
    for i in range(0, len(ciphertext), 2):
        letter1, letter2 = ciphertext[i], ciphertext[i + 1]
        row1, column1 = find_letter_indices(letter1, matrix)
        row2, column2 = find_letter_indices(letter2, matrix)  # Implement first condition.
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
    return "".join(ciphertext)


def create_matrix(key):
    # matrix with 5 rows and 6 columns
    matrix = []
    alphabet = "AĂÂBCDEFGHIÎKLMNOPQRSȘTȚUVWXYZ"
    new_alphabet = ''.join(dict.fromkeys(key + alphabet))

    for i in range(0, 30, 6):
        row = new_alphabet[i:i + 6]
        matrix.append(list(row))

    return matrix


def input_key():
    key = input("Key: ")
    key = key.replace(" ", "")
    while not (romanian_language(key) and len(key) >= 7):
        print("Ensure that the characters are within the range 'A'-'Z' or 'a'-'z' (romanian lang.), and that the key is at least 7 characters long")
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
