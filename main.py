def encrypt(text, key):
    result = ""
    for ch in text:
        if ch.isalpha():
            if ch.isupper():
                result += chr((ord(ch) - 65 + key) % 26 + 65)
            else:
                result += chr((ord(ch) - 97 + key) % 26 + 97)
        else:
            result += ch
    return result


def decrypt(text, key):
    return encrypt(text, -key)


def brute_force(text):
    for key in range(1, 26):
        print("Key", key, ":", decrypt(text, key))


last_result = ""

while True:
    print("\n1) Encryption")
    print("2) Decryption")
    print("3) Brute Force")
    print("4) Exit")
    choice = input("Choose: ")

    if choice == "1":
        text = input("Enter plaintext: ")
        key = int(input("Enter key: "))
        last_result = encrypt(text, key)
        print("Ciphertext:", last_result)

    elif choice == "2":
        text = input("Enter ciphertext (leave empty to use last result): ")
        if text == "":
            text = last_result
        key = int(input("Enter key: "))
        print("Plaintext:", decrypt(text, key))

    elif choice == "3":
        text = input("Enter ciphertext (leave empty to use last result): ")
        if text == "":
            text = last_result
        brute_force(text)

    elif choice == "4":
        break

    else:
        print("Invalid choice")