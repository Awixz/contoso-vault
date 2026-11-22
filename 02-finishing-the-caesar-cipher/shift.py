ALPHABET_SIZE = 26

message: str = input("Message: ")  # "AB$78"
key: int = int(input("Key: "))

ciphertext = ""

# What if the message had symbols to begin with?
# What if the message has lowercase letters?

for letter in message:  # "VWX"
    if "A" <= letter <= "Z":
        shifted = ord(letter) + key  # 89
        shifted = (shifted - ord("A")) % ALPHABET_SIZE + ord("A")
        ciphertext += chr(shifted)
    else:
        ciphertext += letter

print(ciphertext)
