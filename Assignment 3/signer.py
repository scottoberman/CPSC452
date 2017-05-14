import os, random, struct
import sys
from Crypto.Cipher import AES
from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_v1_5
from Crypto.Hash import SHA512
from base64 import b64encode, b64decode

##################################################
# Encrypt the file that has signature
# @param inputFile - file with signature to encrypt
# @param key - aes key to encrypt inputFile
# @return - encrypted data
##################################################
def encrypt(inputFile, key):
	encrypted = None
	#open file with signature embedded
	fileIn = open(inputFile, "r")
	data = fileIn.read()
	fileIn.close()
	print "len of file with sig " + str(len(data))

	# Create an instance of the AES class
	# and initialize the key
	IV = 16 * '\x00'
	aes = AES.new(key, AES.MODE_ECB, IV)
	#encrypt the signature
	encrypted = aes.encrypt(data)
	return encrypted

##################################################
# Encrypt the file that has signature
# @param inputFile - file with signature to encrypt
# @param key - aes key to encrypt inputFile
# @return - encrypted data
##################################################
def decrypt(inputFile, key):
	decrypted = None
	#save signature in string to data
	fileIn = open(inputFile, "r")
	data = fileIn.read()
	fileIn.close()
	# Create an instance of the AES class
	# and initialize the key
	IV = 16 * '\x00'
	aes = AES.new(key, AES.MODE_ECB, IV)
	#encrypt the signature
	decrypted = aes.decrypt(data)
	return decrypted


####################################################
# Saves the encrypted signature to a file
# @param outputFile - the name of the file
# @param data - data want to write to outputFile
####################################################
def saveFile(outputFile, data):
	#save encrypted data to outputFile
	outputFile = open(outputFile, "w")
	outputFile.write(data)
	outputFile.close()
	pass

####################################################
# Embed signature to a file
# @param fileName - the name of the destination file
# @param signature - a signature file to embed
####################################################
def embed(fileName, signature):
	#read signature file to data
	fileIn = open(signature,"r")
	data = fileIn.read()
	fileIn.close()
	#embed data to fileName
	fileOut=open(fileName,"r+a")
	data2=fileOut.read()
	print len(data)
	print len(data2)
	#check for input strings that must be a multiple of 16 in length and insert pad
	num = (len(data)+len(data2))/16
	print (len(data)+len(data2))
	if ((len(data)+len(data2)) - num*16 > 0):
		dif = (num+1)*16 - len(data) - len(data2)
		pad = ' ' * dif
		print "adding pads to data"
		print "data len is now " + str(len(data) + len(data2))
	#embed data to fileName
	fileOut.write(pad)
	fileOut.write(data)
	fileOut.close()
	pass


##################################################
# Loads the RSA key object from the location
# @param keyPath - the path of the key
# @return - the RSA key object with the loaded key
##################################################
def loadKey(keyPath):

	# The RSA key
	key = None

	# Open the key file
	with open(keyPath, 'r') as keyFile:

		# Read the key file
		keyFileContent = keyFile.read()

		# Decode the key
		decodedKey = b64decode(keyFileContent)

		# Load the key
		key = RSA.importKey(decodedKey)

	# Return the key
	return key


##################################################
# Signs the string using an RSA private key
# @param sigKey - the signature key
# @param string - the string
##################################################
def digSig(sigKey, string):

	# TODO: return the signature of the file
	return sigKey.sign(string, '')
	pass

##########################################################
# Returns the file signature
# @param fileName - the name of the file
# @param privKey - the private key to sign the file with
# @return fileSig - the file signature
##########################################################
def getFileSig(fileName, privKey):
	signedHash = None
	# TODO:
	# 1. Open the file
	with open(fileName, 'r') as theFile:
		# 2. Read the contents
		fileContent = theFile.read()
		# 3. Compute the SHA-512 hash of the contents
		dataHash = SHA512.new(fileContent).hexdigest()
		# 4. Sign the hash computed in 4. using the digSig() function
		# you implemented.
		signedHash = digSig(privKey, dataHash)
	# 5. Return the signed hash; this is your digital signature
	return signedHash
	pass

###########################################################
# Verifies the signature of the file
# @param fileName - the name of the file
# @param pubKey - the public key to use for verification
# @param signature - the signature of the file to verify
##########################################################
def verifyFileSig(fileName, pubKey, signature):
	verification = None
	# TODO:
	# 1. Read the contents of the input file (fileName)
	with open(fileName, 'r') as theFile:
		fileContent = theFile.read()
		# 2. Compute the SHA-512 hash of the contents
		dataHash = SHA512.new(fileContent).hexdigest()
		# 3. Use the verifySig function you implemented in
		# order to verify the file signature
		verification = verifySig(dataHash, signature, pubKey)
	# 4. Return the result of the verification i.e.,
	return verification
	# True if matches and False if it does not match
	pass

############################################
# Saves the digital signature to a file
# @param fileName - the name of the file
# @param signature - the signature to save
############################################
def saveSig(fileName, signature):

	# TODO:
	# Signature is a tuple with a single value.
	# Get the first value of the tuple, convert it
	# to a string, and save it to the file (i.e., indicated
	# by fileName)

	# get first value from tuple
	firstVal = str(signature[0])
	# open file
	theFile = open(fileName, 'w')
	# write firstVal to file
	theFile.write(firstVal)
	# close file
	theFile.close()
	pass

###########################################
# Loads the signature and converts it into
# a tuple
# @param fileName - the file containing the
# signature
# @return - the signature
###########################################
def loadSig(fileName):

	theTuple = None
	# TODO: Load the signature from the specified file.
	# Open the file, read the signature string, convert it
	# into an integer, and then put the integer into a single
	# element tuple
	with open(fileName, 'r') as theFile:
		fileContent = int(theFile.read())
		theTuple = (fileContent,)
	return theTuple
	pass

#################################################
# Verifies the signature
# @param theHash - the hash
# @param sig - the signature to check against
# @param veriKey - the verification key
# @return - True if the signature matched and
# false otherwise
#################################################
def verifySig(theHash, sig, veriKey):

	# TODO: Verify the hash against the provided
	# signature using the verify() function of the
	# key and return the result
	return veriKey.verify(theHash, sig)
	pass

# The main function
def main():
	# Make sure that all the arguments have been provided
	if len(sys.argv) < 5:
		print "USAGE: " + sys.argv[0] + " <KEY FILE NAME> <SIGNATURE FILE NAME> <INPUT FILE NAME> <MODE> <AES> <KEY>"
		exit(-1)

	# The key file
	keyFileName = sys.argv[1]

	# Signature file name
	sigFileName = sys.argv[2]

	# The input file name
	inputFileName = sys.argv[3]

	# The mode i.e., sign or verify
	mode = sys.argv[4]

	# TODO: Load the key using the loadKey() function provided.
	loadedKey = loadKey(keyFileName)

	# We are signing
	if mode == "sign":

		# TODO: 1. Get the file signature
		sig = getFileSig(inputFileName, loadedKey)
		print "Signature: " + str(sig[0])
		#       2. Save the signature to the file
		saveSig(sigFileName, sig)

		print "Signature saved to file ", sigFileName

        	#Extra credit: option to encrypt the file with signature using AES
        	#verify using AES
		if len(sys.argv) > 5:
			if (sys.argv[5] == "AES" or sys.argv[5] == "aes"):
				#verify key
				if len(sys.argv) < 7:
					print "Please enter AES key to encrypt file"
					print "USAGE: " + sys.argv[0] + " <KEY FILE NAME> <SIGNATURE FILE NAME> <INPUT FILE NAME> <MODE> AES <KEY>"
					exit(-1)
				#aes key
				key = sys.argv[6]
				#embed signature to file
				embed(inputFileName, sigFileName)
				print "Embedded signature to the file"
				#encrypt signature file
				encrypted = encrypt(inputFileName, key)
				print "Encrypted successfully"
				#save encrypted file
				saveFile(inputFileName, encrypted)
				print "Saved encrypted file to encryped.txt"
        		else:	
				if (sys.argv[5] != ""):
					print "To encrypt file, must use AES and AES_KEY"
					print "USAGE: " + sys.argv[0] + " <KEY FILE NAME> <SIGNATURE FILE NAME> <INPUT FILE NAME> <MODE> AES <KEY>"
					exit(-1)

	# We are verifying the signature
	elif mode == "verify":
		#Extra credit: option to decrypt the file using AES
        	#verify using AES
		if len(sys.argv) > 5:
        		if (sys.argv[5] == "AES" or sys.argv[5] == "aes" ):
                		#verify key
                		if len(sys.argv) < 7:
					print "Please enter AES key to encrypt file"
					print "USAGE: " + sys.argv[0] + " <KEY FILE NAME> <SIGNATURE FILE NAME> <INPUT FILE NAME> <MODE> AES <KEY>"
					exit(-1)
                		#aes key
                		key = sys.argv[6]
                		#decrypt encrypted file
                		decrypted = decrypt(inputFileName, key)
               		 	#remove signature from orignal data
                		signature = "12345"
                		original = decrypted.replace(signature, "")
	                        #remove padded values in original
				while (original[-1] == " "):
					original = original.replace(original[-1],"")
                		#save signature to a file
                		saveFile(sigFileName, signature)
                		#save original data to a file
                		saveFile(inputFileName, original)
                
		# TODO Use the verifyFileSig() function to check if the
		# signature in the signature file matches the
		# signature of the input file
		theSig = loadSig(sigFileName)
		inputSig = verifyFileSig(inputFileName, loadedKey, theSig)

		if (inputSig):
			print "Signatures Match!"
		else:
			print "Signatures Do Not Match..."

		pass
	else:
		print "Invalid mode ", mode

### Call the main function ####
if __name__ == "__main__":
	main()
