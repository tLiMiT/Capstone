


###################################################
#### Category: Constant
# A dummy list of characters and probabilities
# used for testing and examples. Character percentages
# from http://www.data-compression.com/english.html
###################################################
LETTER_FREQ = {
	('A',): 0.0651738,
	('B',): 0.0124248,
	('C',): 0.0217339,
	('D',): 0.0349835,
	('E',): 0.1041442,
	('F',): 0.0197881,
	('G',): 0.0158610,
	('H',): 0.0492888,
	('I',): 0.0558094,
	('J',): 0.0009033,
	('K',): 0.0050529,
	('L',): 0.0331490,
	('M',): 0.0202124,
	('N',): 0.0564513,
	('O',): 0.0596302,
	('P',): 0.0137645,
	('Q',): 0.0008606,
	('R',): 0.0497563,
	('S',): 0.0515760,
	('T',): 0.0729357,
	('U',): 0.0225134,
	('V',): 0.0082903,
	('W',): 0.0171272,
	('X',): 0.0013692,
	('Y',): 0.0145984,
	('Z',): 0.0007836,
	(' ',): 0.1918182
	}


###################################################
#### Category: Core Function
# Takes in dictionary of characters & respective probabilities, and returns
#   a dictionary of those characters huffman-coded
#   (writes code in True-False values in inverted order. That is, first branch
#   is last element.)
###################################################
custom_sort = lambda x: (x[1], len(x[0]))
def huffmanAlgorithm(dict_charProb):
	list_charProb = sorted(
		dict_charProb.iteritems(),
		key=custom_sort,
		reverse=True)
	
	dict_hCode = {}
	while len(list_charProb) > 1:
		temp1 = list_charProb.pop()
		temp2 = list_charProb.pop()
		for it in range(len(temp1[0])):
			if temp1[0][it] in dict_hCode:
				dict_hCode[temp1[0][it]].append(True)
			else:
				dict_hCode[temp1[0][it]] = [True]
		
		for it in range(len(temp2[0])):
			if temp2[0][it] in dict_hCode:
				dict_hCode[temp2[0][it]].append(False)
			else:
				dict_hCode[temp2[0][it]] = [False]
		
		list_charProb.append([temp1[0]+temp2[0], temp1[1]+temp2[1]])
		list_charProb.sort(key=custom_sort, reverse=True)
	
	return dict_hCode

###################################################
#### Category: Core Class
# Implements the Huffman Algorithm. Divides choices
#	based on previous selections.
###################################################
class ChoicePath:
    def __init__(self, d):
        self.hCode = d
        self.hChoices = d
        self.cntr = 0
    
    def setCode(self, d):
        self.hCode = d
        self.hChoices = d
        self.cntr = 0
    
    def getChoices(self):
        return self.hChoices.keys()
    
    def splitChoices(self):
    	return {x:self.hChoices[x][-1-self.cntr] for x in self.hChoices}
    
    def getChoiceCount(self):
        return len(self.hChoices)
    
    def select(self, bool):
    	self.cntr = self.cntr+1
        self.hChoices = {x:self.hChoices[x]
            for x in self.hChoices
            if self.hChoices[x][-self.cntr] == bool}
	
    def reset(self):
        self.cntr = 0
        self.hChoices = self.hCode


