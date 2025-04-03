# decryption.py

def caesar_decrypt(encrypted_text, shift):
    decrypted_text = ''
    for char in encrypted_text:
        if char.isalpha():
            shift_amount = shift % 26
            new_char = chr(((ord(char.lower()) - 97 - shift_amount) % 26) + 97)
            decrypted_text += new_char if char.islower() else new_char.upper()
        else:
            decrypted_text += char
    return decrypted_text

# Example usage:
if __name__ == "__main__":
    encrypted_message = input("Enter the message to decrypt: ")
    shift = int(input("Enter the shift value: "))
    decrypted_message = caesar_decrypt(encrypted_message, shift)
    print("Decrypted Message: ", decrypted_message)
