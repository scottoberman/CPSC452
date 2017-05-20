Write a README file (text file, do not submit a .doc file) which contains
– Names and email addresses of all partners.
– The programming language you used (e.g. Python, Java, or C++)
– How to execute your program.
– Whether you implemented the extra credit.
– Anything special about your submission that we should take note of.

# ASSIGNMENT 3

# NAMES
- Scott Oberman
- Erik  Leinhard
- Khoa Do 
- Andrew Michel aamichel@csu.fullerton.edu
- Phung Tran

# PROGRAMMING LANGUAGE
- PYTHON

# HOW TO EXECUTE
- Create signature of the file
    python signer.py privKey.pem <SIGNATURE FILE NAME> <INPUT FILE NAME> sign

- Verify signature 
    python signer.py pubKey.pem <SIGNATURE FILE NAME> <INPUT FILE NAME> verify

- Embedding signature to the file and encrypt it 
    python signer.py privKey.pem <SIGNATURE FILE NAME> <INPUT FILE NAME> sign AES <KEY>

- Decrypt file and verify signature
    python signer.py pubKey.pem <SIGNATURE FILE NAME> <INPUT FILE NAME> verify AES <KEY>


# KEY FILE NAME:
  - the name of the file that contains the private key if signing or the public key if verifying
- SIGNATURE FILE NAME:
  - The target file where the digital signature (signing) will be written to or the file to load the digital signature (verifying)
- INPUT FILE NAME:
  - The file for which to generate or verify the digital signature
- MODE:
  - sign:
    - Encrypts the generated hash from SHA-512 with the private key
  - verify:
    - Decrypts the signature using the public key and compares it with the SHA-512 hash to verify the data
- AES: 
  - the cipher AES used to indicate whether the user want to embed signature to original file and encrypt it
- KEY: 
  - the key that is used for encrypting the file using AES algorithm

# EXTRA CREDIT
Implemented a functionality such that on signing, embeds the signature in the file and gives the user the option to encrypt the file using AES (with the user-specied specied key). When the file is decrypted, the signature will also be veried and the user will be made aware of the whether it matches. The resulting decrypted file must have the embedded signature removed from it.
