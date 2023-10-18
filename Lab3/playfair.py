# Define the alphabet
alfabet = 'AĂÂBCDEFGHIÎJKLMNOPQRSȘTȚUVWXYZ'


# create a matrix 5x6
def get_matrix(key):
    # add the key to the alphabet and remove duplicates
    alfabet2= alfabet.replace("J", "I")
    new_alphabet = ''.join(dict.fromkeys(key + alfabet2))
    matrix = [list(new_alphabet[i:i + 6]) for i in range(0, len(new_alphabet), 6)]
    for row in matrix:
        print(row)
    return matrix


def find_letter_indices(item, matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == item:
                return i, j


def encrypt(message, matrix):
    while not set(message).issubset(set(alfabet)):
        print("\tInvalid characters")
        message = input("\tInput message (only romanian characters)> ").upper()
        message = message.replace(" ", "")
    # replace J with I, so that the alphabet has 30 letters
    message = message.replace("J", "I")
    message = list(message)

    i = 0
    # for letters that repeat, add X between them
    while i < len(message) - 1:
        if message[i] == message[i + 1]:
            message.insert(i + 1, 'X')
        i += 2
    # last letter does not have a pair, add F
    if len(message) % 2 != 0:
        message.append('F')

    message_list = list(message)

    # rules implementation
    # couple 2 letters
    for i in range(0, len(message_list), 2):
        letter1, letter2 = message_list[i], message_list[i + 1]
        row1, col1 = find_letter_indices(letter1, matrix)
        row2, col2 = find_letter_indices(letter2, matrix)
        # when letters and on the same row, se muta cu o pozitie la dreapta
        if row1 == row2:
            message_list[i] = matrix[row1][(col1 + 1) % 6]
            message_list[i + 1] = matrix[row2][(col2 + 1) % 6]
        # when letters and on the same column se muta cu o pozitie in joc pe coloana
        elif col1 == col2:
            message_list[i] = matrix[(row1 + 1) % 5][col1]
            message_list[i + 1] = matrix[(row2 + 1) % 5][col2]
        # when letters are on different columns and rows, pozitille pe coloana se schimba
        else:
            message_list[i] = matrix[row1][col2]
            message_list[i + 1] = matrix[row2][col1]

    # Convert the list back to a string
    encrypted_message = "".join(message_list)

    return encrypted_message


def decrypt(ciphertext, matrix):
    while not (set(ciphertext).issubset(set(alfabet)) not in ciphertext):
        print("\tInvalid characters")
        ciphertext = input("\tInput the cryptogram (only romanian characters) >").upper()
        ciphertext = ciphertext.replace(" ", "")
    ciphertext_list = list(ciphertext)

    # rules implementation
    # couple 2 letters
    for i in range(0, len(ciphertext_list), 2):
        letter1, letter2 = ciphertext_list[i], ciphertext_list[i + 1]
        row1, col1 = find_letter_indices(letter1, matrix)
        row2, col2 = find_letter_indices(letter2, matrix)

        # when letters and on the same row
        if row1 == row2:
            ciphertext_list[i] = matrix[row1][(col1 - 1) % 6]
            ciphertext_list[i + 1] = matrix[row2][(col2 - 1) % 6]
        # when letters and on the same column
        elif col1 == col2:
            ciphertext_list[i] = matrix[(row1 - 1) % 5][col1]
            ciphertext_list[i + 1] = matrix[(row2 - 1) % 5][col2]
        # when letters are on different columns and rows
        else:
            ciphertext_list[i] = matrix[row1][col2]
            ciphertext_list[i + 1] = matrix[row2][col1]

    decrypted_message = "".join(ciphertext_list)
    # eliminate the added letters
    decrypted_message = decrypted_message.replace("X", "")

    if decrypted_message.endswith("F"):
        decrypted_message = decrypted_message[:-1]

    return decrypted_message


def get_key():
    while True:
        key = input("Key: ").upper().replace(" ", "").replace("J", "I")
        if set(key).issubset(set(alfabet)) and len(key) >= 7:
            return ''.join(dict.fromkeys(key))
        else:
            print("Invalid key (min 7 characters)")


if __name__ == "__main__":
    print('Choose:\n ''1 - Encryption  ''2 - Decryption  3 - Exit\n')

    while True:
        option = input('Action: ')
        if option == '1':
            print('Encryption')
            key = get_key()
            message = input('Message = ').upper()
            message = message.replace(" ", "")
            matrix = get_matrix(key)
            emsg = encrypt(message, matrix)
            print('\t message = ' + emsg)
        elif option == '2':
            print('Decryption')
            key = get_key()
            c = input('Input the cryptogram > ').upper()
            c = c.replace(" ", "")
            c = list(c)
            matrix = get_matrix(key)
            dmsg = decrypt(c, matrix)
            print("\tDecrypted message: " + dmsg)

        elif option == "3":
            break
