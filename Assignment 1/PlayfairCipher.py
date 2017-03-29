import sys
from CipherInterface import CipherInterface

class PlayfairCipher(CipherInterface):

	#Assume that key has NO repeats after filling out RedundantChar with ReplaceChar
	KeyMatrixDimension = 5;
	FillerChar = 'x';
	RedundantChar = 'j';
	ReplaceChar = 'i';
	#J and L are considered =
	AlphaLookup = "abcdefghiklmnopqrstuvwxyz";
	
	KeyMatrix = [];
	
	def __init__(self):
		super().__init__("PlayfairCipher");
	
	def setKey(self, key):
		status = super().setKey(key);
	
		self.KeyMatrix = self.buildKeyMatrix(key);
	
		return status;
	
	def encrypt(self, plaintext):
		encryptedData = "";
		
		pairList = self.buildPlaintextPairList(plaintext);
		#print(pairList);
		#print(self.KeyMatrix);
	
		for pair in pairList:
			coord0 = self.getCoordInMatrix(self.KeyMatrix, pair[0]);
			coord1 = self.getCoordInMatrix(self.KeyMatrix, pair[1]);
			
			encCoord0 = [];
			encCoord1 = [];
			#if same row
			if (coord0[0] == coord1[0]):
				encCoord0.append(coord0[0]);
				encCoord0.append((coord0[1]+1)%self.KeyMatrixDimension);
	
				encCoord1.append(coord1[0]);
				encCoord1.append((coord1[1]+1)%self.KeyMatrixDimension);
	
			#if same col
			elif (coord0[1] == coord1[1]):
				
				encCoord0.append((coord0[0]+1)%self.KeyMatrixDimension);
				encCoord0.append(coord0[1]);
	
				encCoord1.append((coord1[0])+1)%self.KeyMatrixDimension;
				encCoord1.append(coord1[1]);
	
			else:
				encCoord0.append(coord0[0]);
				encCoord0.append(coord1[1]);
	
				encCoord1.append(coord1[0]);
				encCoord1.append(coord0[1]);
			#if (coord0[0]
	
			encryptedData += self.KeyMatrix[encCoord0[0]][encCoord0[1]] + self.KeyMatrix[encCoord1[0]][encCoord1[1]];
		#for pair
	
		return encryptedData;
	#def encrypt
	
	def decrypt(self, ciphertext):
		decryptedData = "";
	
		pairList = self.buildCipertextPairList(ciphertext);
		#print(pairList);
		#print(self.KeyMatrix);
	
		for pair in pairList:
			coord0 = self.getCoordInMatrix(self.KeyMatrix, pair[0]);
			coord1 = self.getCoordInMatrix(self.KeyMatrix, pair[1]);
			
			decCoord0 = [];
			decCoord1 = [];
			#if same row
			if (coord0[0] == coord1[0]):
				decCoord0.append(coord0[0]);
				decCoord0.append((self.KeyMatrixDimension-1) if (coord0[1]==0) else coord0[1]-1);
	
				decCoord1.append(coord1[0]);
				decCoord1.append((self.KeyMatrixDimension-1) if (coord1[1]==0) else coord1[1]-1);
	
			#if same col
			elif (coord0[1] == coord1[1]):
				
				decCoord0.append((self.KeyMatrixDimension-1) if (coord0[0]==0) else coord0[0]-1);
				decCoord0.append(coord0[1]);
	
				decCoord1.append((self.KeyMatrixDimension-1) if (coord1[0]==0) else coord1[0]-1);
				decCoord1.append(coord1[1]);
	
			else:
				decCoord0.append(coord0[0]);
				decCoord0.append(coord1[1]);
	
				decCoord1.append(coord1[0]);
				decCoord1.append(coord0[1]);
			#if (coord0[0]
	
			decryptedData += self.KeyMatrix[decCoord0[0]][decCoord0[1]] + self.KeyMatrix[decCoord1[0]][decCoord1[1]];
		#for pair
	
		return decryptedData;
	
	def buildKeyMatrix(self, data):
		matrix = [];
		modifiedKey = data.replace(self.RedundantChar, self.ReplaceChar);
		keyLength = len(modifiedKey);
		
		for i in range(0, self.KeyMatrixDimension):
			matrix.append([]);
	
		row = 0;
		col = 0;
		index = 0;
		while index<keyLength-1:
			#in slicing the last item is not included in the array
			subKey = list(modifiedKey[index:index+self.KeyMatrixDimension]);
			
			matrix[row] = subKey;
			index += len(subKey);
			row += 1;
			col += len(subKey);
		#while index
	
		while row < self.KeyMatrixDimension:
			#Now that data is overlayed, use the AlphaLookup to fill out the rest
			if (len(matrix[row]) >= self.KeyMatrixDimension):
				row += 1;
				col = 0;
	
			for alpha in self.AlphaLookup:
				coord = self.getCoordInMatrix(matrix, alpha);
	
				if (len(coord) <= 0):
					matrix[row].append(alpha);
					if (len(matrix[row])>=self.KeyMatrixDimension):
						break;
					col += 1;
	
			#for alpha

			row += 1;
			col = 0;
		#while row
	
		return matrix;
	#def buildKeyMatrix
	
	def buildPlaintextPairList(self, plaintext):
		pairCount = 2;
		pairList = [];
		modifiedPlaintext = plaintext.replace(self.RedundantChar, self.ReplaceChar);
	
		index = 0;
		length = len(modifiedPlaintext);
		while index<=length-1:
			pair = list(modifiedPlaintext[index:index+pairCount]);
	
			#if only one item, fill with filler
			if (len(pair) <= 1):
				pair.append(self.FillerChar);
				index += 1;
			elif (pair[0] == pair[1]):
				#go back index wise do to double character
				index -= 1;
				pair[1] = self.FillerChar;
			else:
				index += pairCount;
			#if (len(pair)
	
			pairList.append(pair);
		#while index
	
		return pairList;
	#def buildPlaintextPairList
	
	def buildCipertextPairList(self, ciphertext):
		pairCount = 2;
		pairList = [];
	
		index = 0;
		length = len(ciphertext);
		while index<=length-1:
			pair = list(ciphertext[index:index+pairCount]);
			index += pairCount;
	
			pairList.append(pair);
		#while index
	
		return pairList;
	#def buildCipertextPairList
	
	def getCoordInMatrix(self, matrix, itemToFind):
		coord = [];
	
		row = 0;
		for rowItem in matrix:
			col = self.findIndex(rowItem, itemToFind[0]);
			if (col >= 0):
				coord = [row, col];
				break;
			row += 1;
		#for rowItem
	
		return coord;
	
	def findIndex(self, lst, itemToFind):
		index = -1;
	
		for i in range(len(lst)):
			if (lst[i] == itemToFind):
				index = i;
				break;
		#for i
		
		return index;
	
#end PlayfairCipher
