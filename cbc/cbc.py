def encrypt(message, shared_key, iv):
    encrypted_message = ""
    vector = iv
    for char in message:
        encrypted_char = (ord(char) ^ vector) ^ shared_key
        vector = encrypted_char
        encrypted_message += f"{encrypted_char:03d}"
        print(f"Character {char} is encrypted as {encrypted_char:03d}")
    return encrypted_message

def decrypt(encrypted_message, shared_key, iv):
    decrypted_message = ""
    vector = iv
    for i in range(len(encrypted_message)//3):
        encrypted_char = encrypted_message[i*3:i*3+3:]
        decrypted_char = (int(encrypted_char) ^ shared_key) ^ vector
        vector = int(encrypted_char)
        decrypted_message += chr(decrypted_char)
        print(f"Character {encrypted_char} is decrypted as {chr(decrypted_char)}")
    return decrypted_message