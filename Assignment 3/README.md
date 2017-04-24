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
- Khoa
- Andrew Michel aamichel@csu.fullerton.edu

# PROGRAMMING LANGUAGE
- PYTHON

# HOW TO EXECUTE
python signer.py <KEY FILE NAME> <SIGNATURE FILE NAME> <INPUT FILE NAME> <MODE>

- KEY FILE NAME:
  - the name of the file that contains the private key if signing or the public key if verifying
- SIGNATURE FILE NAME:
  - The target file where the digital signature (singing) will be written to or the file to load the digital signature (verifying)
- INPUT FILE NAME:
  - The file for which to generate or verify the digital signature
- MODE:
  - sign:
    - Encrypts the generated hash from SHA-512 with the private key
  - verify:
    - Decrypts the signature using the public key and compares it with the SHA-512 hash to verify the data

# EXTRA CREDIT
- ANYONE WANNA DO THIS??
