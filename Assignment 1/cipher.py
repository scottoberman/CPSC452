import sys
from CipherInterface import CipherInterface
from PlayfairCipher import PlayfairCipher
from RowTranspositionCipher import RowTranspositionCipher
from RailFenceCipher import RailFenceCipher
from VigenreCipher import VigenreCipher
from CaesarCipher import CaesarCipher

try:
	
	cipherName = (sys.argv[1]).lower();
	cipherKey = sys.argv[2];
	cipherOperation = (sys.argv[3]).lower();
	inputFile = sys.argv[4];
	outputFile = sys.argv[5];
	
	with open(inputFile, "r") as inputFilePtr:
		inputFileData = inputFilePtr.read();
	 
	if (cipherName == "plf"):
		cipher = PlayfairCipher();
	elif (cipherName == "rts"):
		cipher = RowTranspositionCipher();
	elif (cipherName == "rfc"):
		cipher = RailFenceCipher();
	elif (cipherName == "vig"):
		cipher = VigenreCipher();
	elif (cipherName == "ces"):
		cipher = CaesarCipher();
	else:
		cipher = PlayfairCipher();
	#end if (cipherName
	
	#DEBUGGING
	print("cipherName =", cipherName);
	print("cipherKey =", cipherKey);
	print("cipherOperation =", cipherOperation);
	print("inputFile =", inputFile);
	print("outputFile =", outputFile);
	
	print("encrypt: ", cipher.CipherName);
	#DEBUGGING
	
	cipher.setKey(cipherKey);
	
	if (cipherOperation == "enc"):
		outputFileData = cipher.encrypt(cipher.cleanInput(inputFileData));
	elif (cipherOperation == "dec"):
		outputFileData = cipher.decrypt(cipher.cleanInput(inputFileData));
	else:
		outputFileData = cipher.encrypt(cipher.cleanInput(inputFileData));
	
	with open(outputFile, "w") as outputFilePtr:
		outputFilePtr.write(outputFileData);
	
except ValueError:
	print("Please supply arguments");
