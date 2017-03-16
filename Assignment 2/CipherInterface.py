import sys

class CipherInterface:
	CipherName = "";
	CipherKey = "";
	
	def __init__(self, name):
			self.CipherName = name;
			
	def setKey(self, key):
		self.CipherKey = key;
		return True;

	def encrypt(self, plaintext):
		return "";
	
	def decrypt(self, ciphertext):
		return "";
	
	def cleanInput(self, data):
		return (data.strip('\n')).strip('\t');
	
#end CipherInterface