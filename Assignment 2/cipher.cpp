#include "CipherInterface.h"
#include "DES.h"
#include "AES.h"
#include <iostream>
#include <fstream>
#include <string>
#include <stdio.h>

using namespace std;
int processFile(CipherInterface* cipher, FILE* inFile, FILE* outFile, int maxBlockSize, const bool& mode);

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
	/*
	fstream infile(inputFile.c_str());
	string file1((istreambuf_iterator<char>(infile)), (istreambuf_iterator<char>()));
	char* file = new char[file1.size()];
	strcpy(file, file1.c_str());

	cout << "Text taken from inputfile: " << file << endl;
	infile.close();
	*/

	/* Create an instance of the DES cipher */
	CipherInterface* cipher = 0 ;

	unsigned char* output = new unsigned char[100];

	if (ciphername == "AES")
	{
	  cipher = new AES();
	}
	else if (ciphername == "DES")
	{
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
	if(cipher->setKey(key))
	{
		/* open file */
		FILE* infile;
		FILE* outfile;
		infile = fopen(inputFile.c_str(), "r");
		outfile = fopen(outputfile.c_str(), "w");
		//ofstream outfile(outputfile.c_str());
		if (function == "ENC")
		{
			if (ciphername == "DES")
			{
				processFile(cipher, infile, outfile, 8, true);
			}
			else
			{
				processFile(cipher, infile, outfile, 16, true);
				//memcpy(output, cipher->encrypt((unsigned char*)file), 16);
				//cout << "Ciphertext: " << output << endl;
			}
		}
		else if (function == "DEC")
		{
			if (ciphername == "DES")
			{
				processFile(cipher, infile, outfile, 8, false);
			}
			else
			{
				processFile(cipher, infile, outfile, 16, false);
				//memcpy(output, cipher->encrypt((unsigned char*)file), 16);
				//cout << "Plaintext: " << output << endl;
			}
		}
		else
		{
		  cerr << "ERROR incorrected option " << function << endl;
		  exit(-1);
		}
		/*
		ofstream outfile(outputfile.c_str());
		outfile << output;
		outfile.close();
		*/
		fclose(outfile);
		cout << "closing outfile" << endl;
		fclose(infile);
		cout << "closing infile" << endl;
	}
	else
	{
		cerr << "ERROR invalid key" << endl;
	}

	return 0;

}

int processFile(CipherInterface* cipher, FILE* inFile, FILE* outFile, int maxBlockSize, const bool& mode)
{
   /* The class pointer is invalid */
   if(!cipher) { fprintf(stderr, "Invalid cipher class!\n"); return -1;}

   /* Invalid file pointers */
   if(!inFile || !outFile) {fprintf(stderr, "One of the files is a NULL!\n"); return -1;}

   /* The number of bytes read */
   int bytesRead = -1;

   /* The file buffer */
   char fileBuffer[maxBlockSize];

   /* Read the entire file */
   while(bytesRead)
   {
       /* Read from the input file */
       bytesRead = fread(fileBuffer, maxBlockSize, 1, inFile);
	   cout << fileBuffer << sizeof(fileBuffer)<< endl;

       /* Something went wrong */
       if(bytesRead < 0)
       {
           fprintf(stderr, "File read failed!\n");
           exit(-1);
       }
	   cout << "Bytes Read " << bytesRead << endl;
       /* We got stuff to process */
       if(bytesRead)
       {
		   cout << "inside bytesread" << endl;
		   unsigned char* output = new unsigned char[9];
           if(mode)
           {
               //PADD
			   cout << "process encryption" << endl;
			   //encrypt
               memcpy(output, cipher->encrypt((unsigned char*)fileBuffer), maxBlockSize);
			   cout << "encryption successfull" << endl;
           }
           else
           {
			   cout << "process decryption" << endl;
			   memcpy(output, cipher->decrypt((unsigned char*)fileBuffer), maxBlockSize);
				//decrypt
				//fwrite
           }
		   fwrite(output, sizeof(char), sizeof(output), outFile);
		   cout << "writing to file " << outFile << endl;
       }
   }
}
