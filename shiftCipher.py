def encrypt(text, shift):
    encrypted_text = []
    for char in text:
        if char.isupper():
            encrypted_character = chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
        elif char.islower():
            encrypted_character = chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
        else:
            encrypted_character = char
        encrypted_text.append(encrypted_character)
    return ''.join(encrypted_text)

def decrypt(encrypted_text, shift):
    return encrypt(encrypted_text, 26 - shift)

def main():
    text = input("Enter the text to encrypt: ")
    shift = int(input("Enter the shift value: "))
    encrypted_text = encrypt(text, shift)
    decrypted_text = decrypt(encrypted_text, shift)
    print("Encrypted Text: ", encrypted_text)
    print("Decrypted Text: ", decrypted_text)

if __name__ == "__main__":
    main()
