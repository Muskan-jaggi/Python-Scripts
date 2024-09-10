alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
            'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
            'w', 'x', 'y', 'z']

def encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char in alphabet:
            idx_in_alpha = alphabet.index(char)
            encrypted_idx = (idx_in_alpha + shift) % len(alphabet)
            encrypted_text += alphabet[encrypted_idx]
        else:
            encrypted_text += char
    print("\nEncrypted Text is:", encrypted_text)

def decrypt(text, shift):
    decrypted_text = ""
    for char in text:
        if char in alphabet:
            idx_in_alpha = alphabet.index(char)
            decrypted_idx = (idx_in_alpha - shift) % len(alphabet)
            decrypted_text += alphabet[decrypted_idx]
        else:
            decrypted_text += char
    print("\nDecrypted Text is:", decrypted_text)

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("\n Type your message:\n").lower()
shift = int(input("\n Type the shift number:\n"))

if direction.lower() == "encode":
    encrypt(text, shift)
elif direction.lower() == "decode":
    decrypt(text, shift)
else:
    print("Invalid input. Please type 'encode' or 'decode'.")



