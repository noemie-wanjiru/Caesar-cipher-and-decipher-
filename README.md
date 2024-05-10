#### Caesar-cipher-and-decipher-
This repository contains python code for a Caesar cipher implementation that can encrypt and decrypt text using a left or right shift, respectively


##### Code Ovverview 
The main file, caesar_cipher.py, contains the following functions:

1. cipher()
    This function encrypts text using a Caesar cipher with a left shift.
    It prompts the user to enter a cipher key and the text to be encrypted.
2. decipher()
    This function decrypts text using a Caesar cipher with a right shift.
    It prompts the user to enter a cipher key and the text to be decrypted.
3. Encryption/Decryption Selection
    The user is prompted to choose between encryption and decryption.
    Depending on the selection, either the cipher() or decipher() function is executed.

##### Cipher Algorithm Details 
The alphabet is represented as a list of lowercase letters from 'a' to 'z'.
Encryption (cipher() Function)
    Each character in the input text is shifted to the left by the specified cipher key.
    Non-alphabetical characters remain unchanged.
Decryption (decipher() Function)
    Each character in the input text is shifted to the right by the specified cipher key to reverse the encryption.
    Non-alphabetical characters remain unchanged.


##### How to Use
1. Input Selection
When prompted, enter your choice (Encryption or Decryption).
2. Cipher Key
Enter an integer as the cipher key when prompted.
3. Text Input
Input the text you want to encrypt or decrypt.

##### Note
Make sure to provide valid inputs as per the instructions to ensure the proper functioning of the cipher.

