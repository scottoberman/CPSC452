import os, random, struct
import sys
from Crypto.Cipher import AES
from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_v1_5
from Crypto.Hash import SHA512
from base64 import b64encode, b64decode

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
		signedHash = digSig(priveKey, dataHash)
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
	return variKey.verify(theHash, sig)
	pass



# The main function
def main():

	# Make sure that all the arguments have been provided
	if len(sys.argv) < 5:
		print "USAGE: " + sys.argv[0] + " <KEY FILE NAME> <SIGNATURE FILE NAME> <INPUT FILE NAME>"
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
		sig = getFileSig(sigFileName, loadedKey)
		#       2. Save the signature to the file
		saveSig(sigFileName, sig)

		print "Signature saved to file ", sigFileName

	# We are verifying the signature
	elif mode == "verify":

		# TODO Use the verifyFileSig() function to check if the
		# signature signature in the signature file matches the
		# signature of the input file
		theSig = loadSig(sigFileName)
		verifyFileSig(inputFileName, loadedKey, theSig)
		pass
	else:
		print "Invalid mode ", mode

### Call the main function ####
if __name__ == "__main__":
	main()
