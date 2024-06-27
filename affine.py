def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def mod_inverse(a, m):
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return -1

def affine_encrypt(plaintext, a, b):
    if gcd(a, 26) != 1:
        raise ValueError("a and 26 are not coprime, encryption will not work.")
    ciphertext = ""
    for char in plaintext:
        if char.isalpha():
            x = ord(char.lower()) - ord('a')
            encrypted_char = (a * x + b) % 26
            if char.isupper():
                ciphertext += chr(encrypted_char + ord('A'))
            else:
                ciphertext += chr(encrypted_char + ord('a'))
        else:
            ciphertext += char
    return ciphertext

def affine_decrypt(ciphertext, a, b):
    a_inv = mod_inverse(a, 26)
    if a_inv == -1:
        raise ValueError("Modular inverse does not exist, decryption will not work.")
    plaintext = ""
    for char in ciphertext:
        if char.isalpha():
            y = ord(char.lower()) - ord('a')
            decrypted_char = (a_inv * (y - b)) % 26
            if char.isupper():
                plaintext += chr(decrypted_char + ord('A'))
            else:
                plaintext += chr(decrypted_char + ord('a'))
        else:
            plaintext += char
    return plaintext

def main():
    plaintext = input("Enter the plaintext: ")
    a = int(input("Enter the value of 'a' (must be coprime with 26): "))
    b = int(input("Enter the value of 'b': "))
    
    print("Plain text:", plaintext)
    
    # Encrypt the plaintext
    encrypted_text = affine_encrypt(plaintext, a, b)
    print("Encrypted:", encrypted_text)
    
    # Decrypt the ciphertext
    decrypted_text = affine_decrypt(encrypted_text, a, b)
    print("Decrypted:", decrypted_text)

if __name__ == "__main__":
    main()
