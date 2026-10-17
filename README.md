# Caesar Cipher

A small command-line Python program that encrypts, decrypts, and brute-forces text using the Caesar cipher.

## Features

1. **Encryption**: enter a plaintext and a key, get the ciphertext.
2. **Decryption**: enter a ciphertext and the key, get the plaintext. Leave the input empty to reuse the last encryption result.
3. **Brute Force**: tries all 25 keys on a ciphertext so you can spot the one that makes sense. Also accepts an empty input to reuse the last result.
4. **Exit**: closes the program.

Uppercase and lowercase letters are both handled. Digits, spaces, and symbols stay as they are.

## How to run

You only need Python 3 installed.

```
python caesar_cipher.py
```

## Example

```
1) Encryption
2) Decryption
3) Brute Force
4) Exit
Choose: 1
Enter plaintext: hello
Enter key: 3
Ciphertext: khoor
```

## How it works

Each letter is shifted forward by the key within the 26-letter alphabet. Decryption shifts the letters back by the same amount.
