# Import necessary libraries
import random
import hashlib
from sympy import isprime
import math


# Function to generate a large prime number with a given number of bits
def generate_large_prime(bits):
    while True:
        num = random.getrandbits(bits)
        num |= (1 << bits - 1) | 1  # Ensure the number is odd and has the correct bit length

        if isprime(num):
            return num


# Function to choose a public exponent for RSA
def choose_public_exponent(phi_n):
    e = 65537  # Commonly used public exponent

    while not (1 < e < phi_n and math.gcd(e, phi_n) == 1):
        e = random.randint(2, phi_n - 1)

    return e


# Message to be signed
msg = "Lupascu Felicia"
print("Message:", msg)

# Hash the message using SHA3-512
hash_object = hashlib.sha3_512()
# Update the hash object with the encoded message
hash_object.update(msg.encode())
# Convert the resulting hash digest (byte string) to an integer (hashed_message) for further processing or storage.
hashed_message = int.from_bytes(hash_object.digest(), byteorder='big')

# Ensure the hash has a specific bit length
hash_size = 512
hashed_message = hashed_message << (hash_size - hashed_message.bit_length())
print("Hashed message:", hashed_message)

# Choose two large prime numbers
bits = 1554
prime1 = generate_large_prime(bits)
prime2 = generate_large_prime(bits)

# Calculate the modulus and Euler's totient function
n = prime1 * prime2
phi_n = (prime1 - 1) * (prime2 - 1)

# Choose a public exponent
e = choose_public_exponent(phi_n)

# Calculate the private exponent
d = pow(e, -1, phi_n)

# Calculate the digital signature using the private exponent
signature = pow(hashed_message, d, n)

# primul calculator trimite n,e,signature si hashed message
# al doilea calculator utilizeaza formula Verification = powermod( signature, e,n,)

# Verify the signature using the public exponent
verification = pow(signature, e, n)

# Print the result of signature verification
print("Signature Verification Result:", verification == hashed_message)
