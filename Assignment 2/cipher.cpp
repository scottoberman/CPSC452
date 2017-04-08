#include "CipherInterface.h"
#include "DES.h"
#include "AES.h"
#include <iostream>
#include <fstream>
#include <string>
#include <stdio.h>

using namespace std;

int processFile(CipherInterface * cipher, FILE * inFile, FILE * outFile,
    int maxBlockSize, const bool & mode);

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
          memcpy(output, cipher->encrypt((unsigned char*)file), 16);
          //attempted input file block padding
          //processFile(cipher, infile, outfile, 16, true);
	  cout << "Ciphertext: " << output << endl;
	}
	else if (function == "DEC")
	{
	  cout << "Function is decryption" << endl;
	  memcpy(output, cipher->decrypt((unsigned char*)file), 16);
          //attempted input file block padding
          //processFile(cipher, infile, outfile, 16, false);
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

int processFile(CipherInterface * cipher, FILE * inFile, FILE * outFile,
    int maxBlockSize, const bool & mode)
{
    // Invalid class pointer
    if (!cipher)
    {
        fprintf(stderr, "Invalid cipher class\n");
        return -1;
    }
    
    // Invalid file pointer
    if (!inFile) || !outFile)
    {
        fprintf(stderr, "One of the files is a NULL!\n");
        return -1;
    }
    
    int bytesRead = -1;
    
    // File buffer
    char fileBuffer[maxBlockSize];
    
    while(bytesRead)
    {
        bytesRead = fread(fileBuffer, maxBlockSize, 1, inFile);
        if (bytesRead < 0)
        {
            fprintf(sterr, "Error with file read\n");
            exit -1;
        }
        if (bytesRead)
        {   // mode is encrypt
            if(!mode)
            {   // bytesRead is not 16
                if (bytesRead < maxBlockSize)
                {
                    memcpy(fileBuffer, cipher->encrypt((unsigned char*)file));
                    memcpy(fileBuffer, "0", (maxBlockSize - bytesRead));
                    fwrite(fileBuffer, 16, 1, inFile);
                    return 0;
                }
                else
                {
                    memcpy(fileBuffer, cipher->encrypt((unsigned char*)file));
                    cipher->encrypt((unsigned char*)file);
                    fwrite(fileBuffer, 16, 1, inFile);
                    return 0;
                }
            }
            else // mode is decrypt
            {
                memcpy(fileBuffer, cipher->decrypt((unsigned char*)file));
                memcpy(fileBuffer, "0", (maxBlockSize - bytesRead));
                fwrite(fileBuffer, 16, 1, outFile);
                return 0;
            }
        }
    }
}