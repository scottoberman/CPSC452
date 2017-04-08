#include "AES.h"
#include <iostream>

using namespace std;

/**
 * Sets the key to use
 * @param key - the first byte of this represents whether
 * to encrypt or to decrypt. 00 means encrypt and any other
 * value to decrypt.  Then come the bytes of the 128-bit key
 * (should be 16 of them).
 * @return - True if the key is valid and False otherwise
 */
bool AES::setKey(const unsigned char* keyArray)
{
	
	// TODO: AES implementation of openssl cares about whether
	// you are encrypting or decrypting when setting the key.
	// That is, when encrypting you use function AES_set_encrypt_key(...)
	// and when decrypting AES_set_decrypt_key(...).
	//
	// One way to solve this problem is to pass in a 17 byte key, where
	// the first byte is used to indicate whether we are encrypting or
	// decrypting. E.g., if the first byte is 0, then use AES_set_encrypt_key(...).
	// Otherwise, use AES_set_decrypt_key(...).  The rest of the bytes in the
	// array indicate the 16 bytes of the 128-bit AES key.
	//
	// Both functions return 0 on success and other values on faliure.
	// For documentation, please see https://boringssl.googlesource.com/boringssl/+/2623/include/openssl/aes.h
	// and aes.cpp example provided with the assignment.
	if (keyArray[0] == '0' && strlen((char*)keyArray) == 16) // If encrypting...
	{
		return (AES_set_encrypt_key(keyArray + 1, 128, &key) == 0);
	}
	else if (keyArray[0] == '1' && strlen((char*)keyArray) == 16) // If decrypting...
	{
		return (AES_set_decrypt_key(keyArray + 1, 128, &key) == 0);
	}
	else // Error case should not happen
	{
		printf("AES::SetKey: Invalid first byte\n");
		if (1)
		{
			cout << "KeySize is " << strlen((char*)keyArray);
		}

		return false;
	}	
}

/**	
 * Encrypts a plaintext string
 * @param plaintext - the plaintext string
 * @return - the encrypted ciphertext string
 */
unsigned char* AES::encrypt(const unsigned char* plainText)
{
	//TODO: 1. Dynamically allocate a block to store the ciphertext.
	unsigned char* cipherText = new unsigned char[strlen((char*)plainText) + 1];
	cout << "plainTextEnc size is: " << strlen((char*)plainText) << endl;
	cout << "cipherTextEnc size is: " << strlen((char*)plainText) + 1 << endl;
	//	2. Use AES_ecb_encrypt(...) to encrypt the text (please see the URL in setKey(...)
	//	and the aes.cpp example provided.

	// Since AES_ebc_encrypt works on 16 byte blocks, we must
	// move through the plaintext in 16 byte increments
	int x;
	for (x = 0; x < strlen((char*)plainText); x += 16)
	{
		AES_ecb_encrypt(plainText + x, cipherText + x, &key, AES_ENCRYPT);
	}
	cipherText[x] = 0; // For null terminator
	// 	3. Return the pointer to the ciphertext
		
	return cipherText;	
}

/**
 * Decrypts a string of ciphertext
 * @param cipherText - the ciphertext
 * @return - the plaintext
 */
unsigned char* AES::decrypt(const unsigned char* cipherText)
{
	
	//TODO: 1. Dynamically allocate a block to store the plaintext.
	unsigned char* plainText = new unsigned char[strlen((char*)cipherText) + 1];
	cout << "plainTextDec size is: " << strlen((char*)cipherText) + 1 << endl;
	cout << "cipherTextDec size is: " << strlen((char*)cipherText) << endl;
	//	2. Use AES_ecb_encrypt(...) to decrypt the text (please see the URL in setKey(...)
	//	and the aes.cpp example provided.

	// Since AES_ebc_encrypt works on 16 byte blocks, we must
	// move through the plaintext in 16 byte increments
	int x;
	for (x = 0; x < strlen((char*)cipherText); x += 16)
	{
		AES_ecb_encrypt(cipherText + x, plainText + x, &key, AES_DECRYPT);
	}
	plainText[x] = 0;
	// 	3. Return the pointer to the plaintext
	return plainText;
}



