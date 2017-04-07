#include <string>
#include "CipherInterface.h"
#include "DES.h"
#include "AES.h"
#include <iostream>

using namespace std;

int main(int argc, char** argv)
{

	/**
	 * TODO: Replace the code below	with your code which can SWITCH
	 * between DES and AES and encrypt files. DO NOT FORGET TO PAD
	 * THE LAST BLOCK IF NECESSARY.
	 *
	 * NOTE: due to the incomplete skeleton, the code may crash or
	 * misbehave.
	 */

	 /* ciphername */
	 string ciphername = argv[1];
	 /* key */
	 unsigned char* key = (unsigned char*)argv[2];
	 /* enc or dec */
	 string function = argv[3];
	 /* inputfile */
	 string inputFile = argv[4];
	 /* outputfile */
	 string outputfile = argv[5];

	 /* extract text from textfile */
	 

	 /* Create an instance of the DES cipher */
	 CipherInterface* cipher = new CipherInterface();

	 /* Error checks */
	 if(!cipher)
	 {
		 fprintf(stderr, "ERROR [%s %s %d]: could not allocate memory\n",
		 __FILE__, __FUNCTION__, __LINE__);
		 exit(-1);
	 }


	  /* Check to see if there are 6 arguments */
	  if (argc != 6)
	  {
		  cout << "ERROR incorrected amount of arguments" << endl;
		  exit(-1);
	  }

	  string ciphertext;
	  string plaintext;

	  if (ciphername == "AES")
	  {
		  cout << "ciphername is AES" << endl;
		  AES* cipher = new AES();
	  }
	  else if (ciphername == "DES")
	  {
		  cout << "Ciphername is DES" << endl;
		  DES* cipher = new DES();
	  }
	  else
	  {
		  fprintf(stderr, "ERROR %s is an incorrect option", ciophername);
	  }

	  if (function == "ENC")
	  {
		  cipher->encrypt();
	  }
	  else if (function == "DES")
	  {
		  cipher->decrypt();
	  }
	  else
	  {
		  cout << "ERROR incorrected option ", function << endl;
		  exit(-1);
	  }

	  /* Set the encryption key
 	  * A valid key comprises 16 hexidecimal
 	  * characters. Below is one example.
 	  * Your program should take input from
 	  * command line.
 	  */
 	  cipher->setKey((unsigned char*)"0123456789abcdef");

	  return 0;

	/* Perform encryption */
	//string cipherText = cipher->encrypt("hello world");

	/* Perform decryption */
	//cipher->decrypt(cipherText);
}
