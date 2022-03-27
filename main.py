from utility import utility
from dhke import dhke
from io_helper import io_helper
from cbc import cbc

# getting inputs from the user
message = input("Enter the message to be encrypted:\n")
alice_private = io_helper.input_integer("Enter the integer private key for Alice:\n")
bob_private = io_helper.input_integer("Enter the integer private key for Bob:\n")
prime_number = io_helper.input_prime("Enter the prime number:\n")
generator = io_helper.input_generator(prime_number, "Enter the generator:\n")
iv = io_helper.input_iv("Enter the IV as integer:\n")

# public key calculation
alice_public = dhke.compute_public(alice_private, generator, prime_number)
print(f"Alice's public key is: {alice_public}")
bob_public = dhke.compute_public(bob_private, generator, prime_number)
print(f"Bob's public key is: {bob_public}")

# shared key calculation
alice_shared = dhke.compute_shared(alice_private, bob_public, prime_number)
print(f"Shared key calculated by Alice {alice_shared}")
bob_shared = dhke.compute_shared(bob_private, alice_public, prime_number)
print(f"Shared key calculated by Bob {bob_shared}")

# encryption
encrypted_message = cbc.encrypt(message, alice_shared, iv)
print(f"Encrypted message by Alice is: {encrypted_message}")

# decryption
decrypted_message = cbc.decrypt(encrypted_message, bob_shared, iv)
print(f"Decrypted message by Bob is: {decrypted_message}")


