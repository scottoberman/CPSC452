#include "CipherInterface.h"
#include "DES.h"
#include "AES.h"
#include <iostream>
#include <fstream>
#include <string>
#include <stdio.h>

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
	cout << "ciphername: " << ciphername << endl;
	/* key */
	unsigned char* key = (unsigned char*)argv[2];
	cout << "key:" << key << endl;
	/* enc or dec */
	string function = argv[3];
	cout << "function:" << function << endl;
	/* inputfile */
	string inputFile = argv[4];
	cout << "inputFile:" << inputFile << endl;
	/* outputfile */
	string outputfile = argv[5];
	cout << "outputfile:" << outputfile << endl;

	/* extract text from textfile */
	fstream infile(inputFile.c_str());
	string file1((istreambuf_iterator<char>(infile)), (istreambuf_iterator<char>()));
	char* file = new char[file1.size()];
	strcpy(file, file1.c_str());

	cout << "Text taken from inputfile: " << file << endl;
	infile.close();

	/* Create an instance of the DES cipher */
	CipherInterface* cipher = 0 ;

	unsigned char* output = new unsigned char[100];

	if (ciphername == "AES")
	{
	  cout << "Ciphername is AES" << endl;
	  cipher = new AES();
	}
	else if (ciphername == "DES")
	{
	  cout << "Ciphername is DES" << endl;
	  cipher = new DES();
	}
	else
	{
	  cerr << "ERROR %s is an incorrect option " << ciphername;
	  exit(-1);
	}

	/* Error checks */
	if(!cipher)
	{
		fprintf(stderr, "ERROR [%s %s %d]: could not allocate memory\n",
		__FILE__, __FUNCTION__, __LINE__);
		exit(-1);
	}

	/* Set the encryption key
	* A valid key comprises 16 hexidecimal
	* characters. Below is one example.
	* Your program should take input from
	* command line.
	*/
	cipher->setKey(key);

	if (function == "ENC")
	{
	  cout << "Function is encryption" << endl;
	  output = cipher->encrypt((unsigned char*)file);
	  cout << "Ciphertext: " << output << endl;
	}
	else if (function == "DES")
	{
	  cout << "Function is decryption" << endl;
	  output = cipher->decrypt((unsigned char*)file);
	  cout << "Plaintext: " << output << endl;
	}
	else
	{
	  cerr << "ERROR incorrected option " << function << endl;
	  exit(-1);
	}

	ofstream outfile(outputfile.c_str());
	outfile << output;
	outfile.close();

	return 0;

}
