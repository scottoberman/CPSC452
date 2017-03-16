import sys
from CipherInterface import CipherInterface

class VigenreCipher(CipherInterface):
	
	def __init__(self):
			super().__init__("VigenreCipher")
	
	def setKey(self, key):
            status = super().setKey(key)
		
            return status;
	
	def encrypt(self, plaintext):
            encryptedData = ""
            convert = 0
            k = 0
            lenKey = len(self.CipherKey)
            lenPt = len(plaintext)

            for i in range(0, lenPt):
                convert = (ord(plaintext[i]) - 97 + ord(self.CipherKey[k]) - 97) % 26
                k = (k + 1) % lenKey
                encryptedData += chr(convert + 97)
                
            #print (encryptedData)
            return encryptedData;
	#def encrypt
	
	def decrypt(self, ciphertext):
            decryptedData = ""
            convert = 0
            k = 0
            lenKey = len(self.CipherKey)
            lenCipherText = len(ciphertext)
            
            for i in range(0, lenCipherText):
                convert = ( abs( (ord(ciphertext[i]) - 97) - ( ord(self.CipherKey[k]) - 97)) ) % 26
                k = (k + 1) % lenKey
                decryptedData += chr(convert + 97)
	
            #print(decryptedData)
            return decryptedData
        #def decrypt
	
#end VigenreCipher
