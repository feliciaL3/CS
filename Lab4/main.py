import random
import string

# Define the initial permutation table for DES
initial_permutation = [58, 50, 42, 34, 26, 18, 10, 2,
                       60, 52, 44, 36, 28, 20, 12, 4,
                       62, 54, 46, 38, 30, 22, 14, 6,
                       64, 56, 48, 40, 32, 24, 16, 8,
                       57, 49, 41, 33, 25, 17, 9, 1,
                       59, 51, 43, 35, 27, 19, 11, 3,
                       61, 53, 45, 37, 29, 21, 13, 5,
                       63, 55, 47, 39, 31, 23, 15, 7]


# Function to perform permutation using the initial_permutation table
def permute(bits):
    permutation = ''
    for i in range(64):
        permutation += bits[initial_permutation[i] - 1]
    return permutation


# Function to input a message of 8 characters
def message_input():
    while True:
        msg = input('Message - 8 characters: ')
        if len(msg) == 8:
            return msg
        else:
            print('The message should be 8 characters long. Try again.')


while True:
    try:
        print('===== Choose an input method: =====:\n1. Manual input\n2. Random string\n3. Exit')
        opt = int(input('>'))
        if opt == 1 or opt == 2:
            message = ''
            if opt == 1:
                message = message_input()
            elif opt == 2:
                # Generate a random message with letters, digits, and punctuation
                characters = string.ascii_letters + string.digits + string.punctuation
                message = ''.join(random.choice(characters) for i in range(8))
                print('Message: ', message)

            # Convert the message to its binary representation
            message = ''.join(format(ord(i), '08b') for i in message)
            print('\nMessage in binary format:\n', message, '\n')
            # mesajul initial in binar dar fiecare character separat
            binary_message_4 = ' '.join([message[i:i+4] for i in range(0, len(message), 4)])
            print(binary_message_4)
            print("")

            print('Initial permutation table:')
            for i in range(64):
                print(initial_permutation[i], ' ', end='')
                # Acest segment verifică dacă s-au afișat deja 8 valori (deoarece există 8 coloane în tabel)
                if ((i + 1) % 8) == 0:
                    print()

            # Perform the initial permutation on the binary message
            message = permute(message)
            print('\nMessage after initial permutation:\n', message, '\n')

            # Extract the left half (L1) of the message
            L1 = message[0:32]
            print('L1: ', L1, '\n')

        elif opt == 3:
            exit()
        else:
            print('\nInvalid input.')

    except ValueError:
        print('\nInvalid input.')
