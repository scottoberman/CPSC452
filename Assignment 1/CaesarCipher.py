import sys
from CipherInterface import CipherInterface

class CaesarCipher(CipherInterface):
	ShiftValue = 0;
	
	def __init__(self):
			super().__init__("CaesarCipher");
	
	def setKey(self, key):
		status = super().setKey(key);
	
		self.ShiftValue = int(key);
	
	
		return status;
	
	def encrypt(self, plaintext):
		encryptedData = "";
	
		for i in plaintext:
			encryptedData += self.process(i, self.ShiftValue, 1);
	
		return encryptedData;
	#end def encrypt
	
	def decrypt(self, ciphertext):
		decryptedData = "";
	
		for i in ciphertext:
			decryptedData += self.process(i, self.ShiftValue, -1);
	
		return decryptedData;
	#end def decrypt
	
	def process(self, data, shiftValue, operationIndex):
		alphaLength = 26;
		firstIndex = ord('a');
		index = ord(data)-firstIndex;
	
		return chr(((index+operationIndex*shiftValue)%alphaLength)+firstIndex);
	
#end CaesarCipher
