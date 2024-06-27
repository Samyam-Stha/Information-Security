def vigenere_encrypt(text, key):
    encrypted_text = []
    text_len = len(text)
    key_len = len(key)
    
    for i in range(text_len):
        j = i % key_len
        if text[i].isalpha():
            if text[i].isupper():
                encrypted_character = chr((ord(text[i]) - ord('A') + ord(key[j]) - ord('a')) % 26 + ord('A'))
            else:
                encrypted_character = chr((ord(text[i]) - ord('a') + ord(key[j]) - ord('a')) % 26 + ord('a'))
            encrypted_text.append(encrypted_character)
        else:
            encrypted_text.append(text[i])
    
    return ''.join(encrypted_text)

def vigenere_decrypt(text, key):
    decrypted_text = []
    text_len = len(text)
    key_len = len(key)
    
    for i in range(text_len):
        j = i % key_len
        if text[i].isalpha():
            if text[i].isupper():
                decrypted_character = chr((ord(text[i]) - ord('A') - (ord(key[j]) - ord('a')) + 26) % 26 + ord('A'))
            else:
                decrypted_character = chr((ord(text[i]) - ord('a') - (ord(key[j]) - ord('a')) + 26) % 26 + ord('a'))
            decrypted_text.append(decrypted_character)
        else:
            decrypted_text.append(text[i])
    
    return ''.join(decrypted_text)

def main():
    text = input("Enter the text to encrypt: ")
    key = input("Enter the key: ")
    
    encrypted_text = vigenere_encrypt(text, key)
    print("Encrypted Text: ", encrypted_text)
    
    decrypted_text = vigenere_decrypt(encrypted_text, key)
    print("Decrypted Text: ", decrypted_text)

if __name__ == "__main__":
    main()
