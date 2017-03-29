import sys
import math
from CipherInterface import CipherInterface

class RailFenceCipher(CipherInterface):
	ColumnCount = 0;
	RowCount 	= 0;
	# Key will be depth of rail fence
	
	def __init__(self):
			super().__init__("RailFenceCipher");
	
	def setKey(self, key):
		status = super().setKey(key);
	
		self.RowCount = int(key);
	
		return status;
	
	def encrypt(self, plaintext):
		encryptedData = "";
	
		matrix = self.buildMatrixEnc(plaintext);

		for row in matrix:
			for item in row:
				if(item != 0):
					encryptedData += str(item);
			#end for item
		#end for row
	
		return encryptedData;
	#def encrypt
	
	def decrypt(self, ciphertext):
		decryptedData = "";
		dataReadCount = len(ciphertext);
	
		matrix = self.buildMatrixDec(ciphertext);

		for i in range(self.ColumnCount):
			for j in range(self.RowCount):
				if(dataReadCount > 0):
					decryptedData += str(matrix[j][i]);
					dataReadCount -= 1;

		return decryptedData;
	#def decrypt

	def buildMatrixDec(self, data):
		index, i, j = 0, 0, 0;
		self.ColumnCount = math.ceil(len(data) / self.RowCount);
		matrix = [[0 for y in range(self.ColumnCount)] for x in range(self.RowCount)];
		dataLength = len(data);
		longRowsLeft = dataLength % self.RowCount; # Some rows may be longer than others.
	
		while (longRowsLeft > 0):
			matrix[i][j] = data[index];
			j = (j + 1) % (self.ColumnCount);
			if(j == 0):
				i += 1;
				longRowsLeft -= 1;
			index += 1;

		while (index<dataLength):
			matrix[i][j] = data[index];
			j = (j + 1) % (self.ColumnCount - 1);
			if(j == 0):
				i += 1;
			index += 1;

		return matrix;
	#def buildMatrixEnc
	
	def buildMatrixEnc(self, data):
		index, i, j = 0, 0, 0;
		self.ColumnCount = math.ceil(len(data) / self.RowCount);
		matrix = [[0 for y in range(self.ColumnCount)] for x in range(self.RowCount)];
		dataLength = len(data);
	
		while (index<dataLength):
			matrix[i][j] = data[index];
			i = (i + 1) % (self.RowCount);
			if(i == 0):
				j += 1;
			index += 1;
	
		return matrix;
	#def buildMatrixEnc
	
#end RailFenceCipher
