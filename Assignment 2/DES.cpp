#include "DES.h"
#include <iostream>
/**
 * Sets the key to use
 * @param key - the key to use
 * @return - True if the key is valid and False otherwise
 */
bool DES::setKey(const unsigned char* keyArray)
{
	/**
	 * First let's covert the char string
	 * into an integer byte string
	 */


	/* The key error code */
	int keyErrorCode = -1;

	/* A single byte */
	unsigned char singleByte = 0;

	/* The key index */
	int keyIndex = 0;

	/* The DES key index */
	int desKeyIndex = 0;

	/* Go through the entire key character by character */
	while(desKeyIndex != 8)
	{
		/* Convert the key if the character is valid */
		if((this->des_key[desKeyIndex] = twoCharToHexByte(keyArray + keyIndex)) == 'z')
			return false;

		/* Go to the second pair of characters */
		keyIndex += 2;

		/* Increment the index */
		++desKeyIndex;
	}

	fprintf(stdout, "DES KEY: ");

	/* Print the key */
	for(keyIndex = 0; keyIndex < 8; ++keyIndex)
		fprintf(stdout, "%x", this->des_key[keyIndex]);

	fprintf(stdout, "\n");


	/* Set the encryption key */
	if ((keyErrorCode = DES_set_key_checked(&des_key, &this->key)) != 0)
	{
		fprintf(stderr, "\nkey error %d\n", keyErrorCode);

		return false;
	}

	/* All is well */
	return true;
}

/**
 * Encrypts a plaintext string
 * @param plaintext - the plaintext string
 * @return - the encrypted ciphertext string
 */
unsigned char* DES::encrypt(const unsigned char* plaintext)
{
	cout << "inside encrypt, plaintext = " << plaintext << endl;
	//LOGIC:
	//1. Check to make sure that the block is exactly 8 characters (i.e. 64 bits)
	if (strlen((char*)plaintext) != 8)
	{
		return 0; // Return something indicating an error
	}
	//2. Declate an array DES_LONG block[2];
	DES_LONG block[2];

	unsigned char* pt = new unsigned char[sizeof(plaintext)];
	for (int i = 0; i < sizeof(plaintext); i++)
	{
		pt[i] = plaintext[i];
	}
	cout << pt << endl;
	//3. Use ctol() to convert the first 4 chars into long; store the result in block[0]
	block[0] = ctol(pt); // These casts may not give correct result.

	//4. Use ctol() to convert the second 4 chars into long; store the resul in block[1]
	block[1] = ctol(pt + 4); // These casts may not give correct result

	//5. Perform des_encrypt1 in order to encrypt the block using this->key (see sample codes for details)
    DES_encrypt1(block, &this->key, 1);

	unsigned char* ciphertext = new unsigned char[8];

	//6. Convert the first ciphertext long to 4 characters using ltoc()
	ltoc(block[0], ciphertext);

	//7. Convert the second ciphertext long to 4 characters using ltoc()
	ltoc(block[1], ciphertext + 4);

	//8. Save the results in the the dynamically allocated char array
	// (e.g. unsigned char* bytes = nerw unsigned char[8]).

	//9. Return the pointer to the dynamically allocated array.
	return ciphertext;
}

/**
 * Decrypts a string of ciphertext
 * @param ciphertext - the ciphertext
 * @return - the plaintext
 */
unsigned char* DES::decrypt(const unsigned char* ciphertext)
{
	// Same logic as encrypt(), except in step 5. decrypt instead of encrypting
	//LOGIC:
	//1. Check to make sure that the block is exactly 8 characters (i.e. 64 bits)
	if (strlen((char*)ciphertext) != 8)
	{
		return 0; // Return something indicating an error
	}
	//2. Declate an array DES_LONG block[2];
	DES_LONG block[2];

	unsigned char* ct = new unsigned char[sizeof(ciphertext)];
	for (int i = 0; i < sizeof(ciphertext); i++)
	{
		ct[i] = ciphertext[i];
	}
	//3. Use ctol() to convert the first 4 chars into long; store the result in block[0]
	block[0] = ctol(ct); // These casts may not give correct result.

	//4. Use ctol() to convert the second 4 chars into long; store the resul in block[1]
	block[1] = ctol(ct + 4); // These casts may not give correct result

	//5. Perform des_encrypt1 in order to encrypt the block using this->key (see sample codes for details)
    DES_encrypt1(block, &this->key, 0);


	unsigned char* plaintext = new unsigned char[8];

	//6. Convert the first ciphertext long to 4 characters using ltoc()
	ltoc(block[0], plaintext);

	//7. Convert the second ciphertext long to 4 characters using ltoc()
	ltoc(block[1], plaintext + 4);

	//8. Save the results in the the dynamically allocated char array
	// (e.g. unsigned char* bytes = nerw unsigned char[8]).

	//9. Return the pointer to the dynamically allocated array.
	return plaintext;
}

/**
 * Converts an array of 8 characters
 * (i.e. 4 bytes/32 bits)
 * @param c - the array of 4 characters (i.e. 1-byte per/character
 * @return - the long integer (32 bits) where each byte
 * is equivalent to one of the bytes in a character array
 */
DES_LONG DES::ctol(unsigned char *c)
{
        /* The long integer */
	DES_LONG l;

	l =((DES_LONG)(*((c)++)));
        l = l | (((DES_LONG)(*((c)++)))<<8L);
        l = l | (((DES_LONG)(*((c)++)))<<16L);
        l = l | (((DES_LONG)(*((c)++)))<<24L);
        return l;
};


/**
 * Converts a long integer (4 bytes = 32 bits)
 * into an array of 8 characters.
 * @param l - the long integer to convert
 * @param c - the character array to store the result
 */
void DES::ltoc(DES_LONG l, unsigned char *c)
{
        *((c)++)=(unsigned char)(l&0xff);
        *((c)++)=(unsigned char)(((l)>> 8L)&0xff);
        *((c)++)=(unsigned char)(((l)>>16L)&0xff);
        *((c)++)=(unsigned char)(((l)>>24L)&0xff);
}

/**
 * Converts a character into a hexidecimal integer
 * @param character - the character to convert
 * @return - the converted character, or 'z' on error
 */
unsigned char DES::charToHex(const char& character)
{
	/* Is the first digit 0-9 ? */
	if(character >= '0' && character <= '9')
		/* Convert the character to hex */
		return character - '0';
	/* It the first digit a letter 'a' - 'f'? */
	else if(character >= 'a' && character <= 'f')
		/* Conver the cgaracter to hex */
		return (character - 97) + 10;
	/* Invalid character */
	else return 'z';
}

/**
 * Converts two characters into a hex integers
 * and then inserts the integers into the higher
 * and lower bits of the byte
 * @param twoChars - two charcters representing the
 * the hexidecimal nibbles of the byte.
 * @param twoChars - the two characters
 * @return - the byte containing having the
 * valud of two characters e.g. string "ab"
 * becomes hexidecimal integer 0xab.
 */
unsigned char DES::twoCharToHexByte(const unsigned char* twoChars)
{
	/* The byte */
	unsigned char singleByte;

	/* The second character */
	unsigned char secondChar;

	/* Convert the first character */
	if((singleByte = charToHex(twoChars[0])) == 'z')
	{
		/* Invalid digit */
		return 'z';
	}

	/* Move the newly inserted nibble from the
	 * lower to upper nibble.
	 */
	singleByte = (singleByte << 4);

	/* Conver the second character */
	if((secondChar = charToHex(twoChars[1])) == 'z')
		return 'z';

	/* Insert the second value into the lower nibble */
	singleByte |= secondChar;

	return singleByte;
}
