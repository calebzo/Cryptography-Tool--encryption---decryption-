# encryption.py

def caesar_encrypt(plain_text, shift):
    encrypted_text = ''
    for char in plain_text:
        if char.isalpha():
            shift_amount = shift % 26
            new_char = chr(((ord(char.lower()) - 97 + shift_amount) % 26) + 97)
            encrypted_text += new_char if char.islower() else new_char.upper()
        else:
            encrypted_text += char
    return encrypted_text

# Example usage:
if __name__ == "__main__":
    plain_text = input("Enter the message to encrypt: ")
    shift = int(input("Enter the shift value: "))
    encrypted_message = caesar_encrypt(plain_text, shift)
    print("Encrypted Message: ", encrypted_message)
