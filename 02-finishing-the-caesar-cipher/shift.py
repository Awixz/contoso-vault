
ALPHABET_SIZE: int = 26

message: str = input("Message: ")
key: int = int(input("Key: "))

# Encryption
ciphertext: str = ""

for character in message:
    if "A" <= character <= "Z":
        shifted: int = ord(character) + key
        shifted = ord("A") + (shifted - ord("A")) % ALPHABET_SIZE
        ciphertext += chr(shifted)

    elif "a" <= character <= "z":
        shifted = ord(character) + key
        shifted = ord("a") + (shifted - ord("a")) % ALPHABET_SIZE
        ciphertext += chr(shifted)

    else:
        ciphertext += character

print("Ciphertext:", ciphertext)


# Decryption
plaintext: str = ""

for character in ciphertext:
    if "A" <= character <= "Z":
        shifted = ord(character) - key
        shifted = ord("A") + (shifted - ord("A")) % ALPHABET_SIZE
        plaintext += chr(shifted)

    elif "a" <= character <= "z":
        shifted = ord(character) - key
        shifted = ord("a") + (shifted - ord("a")) % ALPHABET_SIZE
        plaintext += chr(shifted)

    else:
        plaintext += character

print("Plaintext:", plaintext)

# Check the round trip
assert plaintext == message
