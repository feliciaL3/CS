# Import necessary libraries
import hashlib
import random
import math

# Define the message
msg = "Lupascu Felicia"

# Hash the message using SHA3-384
hash_object = hashlib.sha3_384()
hash_object.update(msg.encode())
# Convert the resulting hash digest (byte string) to an integer (hashed_message) for further processing or storage.
hashed_message = int.from_bytes(hash_object.digest(), byteorder='big')

# Ensure the hash has a specific bit length.
hash_size = 384
hashed_message = hashed_message << (hash_size - hashed_message.bit_length())
print("Hashed message:", hashed_message)

# Choose large prime 'p' and generator 'g'
p = 32317006071311007300153513477825163362488057133489075174588434139269806834136210002792056362640164685458556357935330816928829023080573472625273554742461245741026202527916572972862706300325263428213145766931414223654220941111348629991657478268034230553086349050635557712219187890332729569696129743856241741236237225197346402691855797767976823014625397933058015226858730761197532436467475855460715043896844940366130497697812854295958659597567051283852132784468522925504568272879113720098931873959143374175837826000278034973198552060607533234122603254684088120031105907484281003994966956119696956248629032338072839127039
g = 2

# Choose private key 'a' randomly
a = random.randint(1, p - 2)

# Compute public key 'b'
b = pow(g, a, p)

# Loop to generate a valid random value 'k'
while True:
    # Generate a random value 'k'
    k = random.randint(1, p - 2)
    gcd_value = math.gcd(k, p - 1)

    # Ensure 'k' is coprime with 'p-1'
    if gcd_value == 1:
        # Calculate signature components 'r' and 's'
        r = pow(g, k, p)
        # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!REMEMBER FORMULA
        s = (pow(k, -1, p - 1) * (hashed_message - a * r)) % (p - 1)
        signature = (r, s)
        print("Signature:", signature)

        # Save the generated signature for verification
        received_signature = signature
        r_received, s_received = received_signature

        # Verify the signature
        v1 = (pow(b, r_received, p) * pow(r_received, s_received, p)) % p
        v2 = pow(g, hashed_message, p)
        verification = (v1 == v2)

        # Print v1 and v2
        print("v1:", v1)
        print("v2:", v2)
        print("Signature Verification:", verification)
        break

        # primul calculator trimite p,g,b(cheie publica) si semnatura
        # al doilea calculator verifica semnatura  v1=(b^r*r^s) mod p
        #                                           v2=g^hash mod p
        # verifica daca v1=v2
