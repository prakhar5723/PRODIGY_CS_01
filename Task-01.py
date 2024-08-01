def shift_char(char, shift, base):
    return chr((ord(char) - base + shift) % 26 + base)


def encrypt(message, shift):
    return ''.join(
        shift_char(char, shift, 65) if char.isupper() else
        shift_char(char, shift, 97) if char.islower() else
        char
        for char in message
    )


def decrypt(cipher, shift):
    return ''.join(
        shift_char(char, -shift, 65) if char.isupper() else
        shift_char(char, -shift, 97) if char.islower() else
        char
        for char in cipher
    )


def main():
    print("Caesar Cipher to Encrypt/Decrypt")
    while True:
        print("Menu:")
        print("1. Encrypt")
        print("2. Decrypt")
        print("3. Exit")
        mode = int(input("Enter your choice: "))
        if mode == 1:
            message = input("Enter your message: ")
            shift = int(input("Enter shift: "))
            cipher = encrypt(message, shift)
            print("Encrypted: " + cipher)
        elif mode == 2:
            cipher = input("Enter Cipher: ")
            shift = int(input("Enter shift: "))
            print("Message: " + decrypt(cipher, shift))
        elif mode == 3:
            print("Exiting...")
            break
        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()
