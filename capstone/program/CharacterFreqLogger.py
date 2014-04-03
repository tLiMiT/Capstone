import csv
import errno

name_delim = '_'
code_default = 'base'

csv_prefix = 'characterFreq_'
csv_suffix = '.csv'

bin_prefix = 'CharFreqBinary_f_'
bin_extension = '.bin'

half_life = 16000.0
max_mem = 3

CHAR_ORDER = ['\n', ' ', '!', '"', '#', '$', '%', '&', "'", 
	'(', ')', '*', '+', ',', '-', '.', '/', '0', '1', '2', 
	'3', '4', '5', '6', '7', '8', '9', ':', ';', '<', '=', 
	'>', '?', '@', 'C', '[', '\\', ']', '^', '_', '`', 'a', 
	'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 
	'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 
	'x', 'y', 'z', '{', '|', '}', '~']

char_order = CHAR_ORDER

def getCharOrder(filename, decode=True):
	global char_order
	list = []
	with open(filename, 'rb') as csvfile:
		csvReader = csv.reader(csvfile)
		for row in csvReader:
			if len(row) == 1:
				list.append(row[0])
			else:
				print 'Invalid Row:'
				for i in row:
					print i
	if decode:
		list = [ x.decode('string_escape') for x in list ]
	
	char_order = list

def saveCharOrder(filename, encode=True):
	# Checks form of dictionary keys: strings? tuple of strings?
	list = char_order
	if type( list[0] ) is tuple:
		if type( list[0][0] ) is not str:
			pass	#error!!!
	elif type( list[0] ) is str:
		list = [(x,) for x in list]
	else:
		pass	#error!!!
	
	# Encodes escape characters
	if encode:
		list = [ (x[0].encode('string_escape'),) for x in list ]
	
	with open(filename, 'wb') as csvfile:
		csvWriter = csv.writer(csvfile)
		csvWriter.writerows( list )
	

def makefilename(base):
	return bin_prefix + base + bin_extension

##############################################################
##################### CSV Reader/Writer ######################
##############################################################
def writeFreq(filename, dict_freq, encode=True):
	# Checks form of dictionary keys: strings? tuple of strings?
	if type( dict_freq.keys()[0] ) is tuple:
		if type( dict_freq.keys()[0][0] ) is str:
			dict_freq = {x[0]:dict_freq[x] for x in dict_freq}
		else:
			pass	#error!!!
	elif type( dict_freq.keys()[0] ) is not str:
		pass	#error!!!
	
	# Encodes escape characters
	if encode:
		dict_freq = { x.encode('string_escape'):dict_freq[x] 
			for x in dict_freq }
	
	with open(filename, 'wb') as csvfile:
		csvWriter = csv.writer(csvfile)
		csvWriter.writerows( dict_freq.items() )


##############################################################
def readFreq(filename, decode=True):
	temp_dict = {}
	with open(filename, 'rb') as csvfile:
		csvReader = csv.reader(csvfile)
		for row in csvReader:
			if len(row) == 2:
				temp_dict[(row[0],)] = float(row[1])
			else:
				print 'Invalid Row:'
				for i in row:
					print i
	if decode:
		temp_dict = { (x[0].decode('string_escape'),):temp_dict[x]
			for x in temp_dict }
	
	return temp_dict

READWRITE_STANDARD = (readFreq, writeFreq)
##############################################################
#################### CSV Raw Reader/Writer ###################
##############################################################

def writeFreq_raw(filename, dict_freq):
	# Checks form of dictionary keys: strings? tuple of strings?
	if type( dict_freq.keys()[0] ) is tuple:
		if type( dict_freq.keys()[0][0] ) is str:
			dict_freq = {x[0]:dict_freq[x] for x in dict_freq}
		else:
			pass	#error!!!
	elif type( dict_freq.keys()[0] ) is not str:
		pass	#error!!!
	
	with open(filename, 'wb') as csvfile:
		csvWriter = csv.writer(csvfile)
		for char in char_order:
			csvWriter.writerow( (str(dict_freq[char]),)
				if char in dict_freq else '0')

##############################################################
def readFreq_raw(filename):
	temp_dict = {}
	with open(filename, 'rb') as csvfile:
		csvReader = csv.reader(csvfile)
		cntr = 0
		for row in csvReader:
			if cntr == len(char_order):	#error!!!
				break
			elif len(row) == 1:
				temp_dict[(char_order[cntr],)] = float(row[0])
				cntr += 1
			else:	#error!!!
				print 'Invalid Row:'
				for i in row:
					print i
	return temp_dict

READWRITE_RAW = (readFreq_raw, writeFreq_raw)
##############################################################
##################### Binary Reader/Writer ###################
##############################################################
from array import array
num_precision = 'f'

def writeFreq_binary(filename, dict_freq):
	# Checks form of dictionary keys: strings? tuple of strings?
	if type( dict_freq.keys()[0] ) is tuple:
		if type( dict_freq.keys()[0][0] ) is str:
			dict_freq = {x[0]:dict_freq[x] for x in dict_freq}
		else:
			pass	#error!!!
	elif type( dict_freq.keys()[0] ) is not str:
		pass	#error!!!
	
	with open(filename, 'wb') as outfile:
		ord_list = []
		for char in char_order:
			ord_list.append( dict_freq[char]
				if char in dict_freq else 0)
		d_array = array(num_precision, ord_list)
		d_array.tofile(outfile)


def readFreq_binary(filename):
	with open(filename, 'rb') as infile:
		d_array = array(num_precision)
		d_array.fromfile(infile, len(char_order))
		temp_dict = { (char_order[cntr],):d_array[cntr]
			for cntr in range(len(char_order))}
	return temp_dict
		
READWRITE_BINARY = (readFreq_binary, writeFreq_binary)


#################### Escape Key Converter ####################
# Escape to Legible - str.encode('string_escape')
# Legible to Escape - str.decode('string_escape')

##############################################################
#################### Frequency File Updater ##################
##############################################################
# dict_freq - a dictionary list
#	keys - letters observed in message
#	values - count of occurences in messages (NOT %)
def updateFreq(filename, func_ReadWrite, dict_freq):
	# Reads old dictionary from file
	old_dict = {}
	try:
		old_dict = func_ReadWrite[0](filename)
	except IOError as e:
		# Check file existence (non-existence is NOT fatal)
		if e.errno == errno.ENOENT:
			pass
		# Other errors are unforseen
		else:
			raise e
	
	# Creates relative weights of message significance
	size1 = sum(dict_freq.values())
	size2 = half_life
	
	# Creates new dictionary, augmented with new data results
	new_dict = {}
	for char in char_order:
		new_dict[(char,)] = 0
		# Scales down significance of new data
		#	(divide by size1 to convert count value to percentage)
		if (char,) in dict_freq:
			new_dict[(char,)] += dict_freq[(char,)] * (1.0 / (size1+size2))
		# Scales down significance of original data
		#	(values already in percentage form)
		if (char,) in old_dict:
			new_dict[(char,)] += old_dict[(char,)] * (size2 / (size1+size2))

	func_ReadWrite[1](filename, new_dict)

##############################################################
################ Char-to-Cond.-Code Converter ################
##############################################################
#### Category: Text Manipulation shorthand
# Converts a string of characters (which may not be valid in
#	file names) into a string of their respective hex numbers. 
code_unit = 2
def cond_char2code(cond_str):
	# Converts ASCII characters to the string representation
	#	of their hex value, then removes the "0x" prefix
	cond_str = [ hex(ord(sub)).split('x')[1] for sub in cond_str ]
	# Adds zeros to make each number 2 characters long
	cond_str = ['0'*(code_unit-len(sub)) + sub for sub in cond_str]
	# Concatenates, then returns result
	return ''.join(cond_str)

##############################################################
################## Message Frequency Counter #################
##############################################################
#### Category: Core Function
# Cycles through message and counts all conditional character 
#	occurrences in the message.
# (Note - For accommodating the caps-lock key, format message
#	before sending through this function.)
def countMessageFreq(message):
	# Pre-analysis formatting
	message = '\x02' + message
	
	cond_freq = {}
	for length in range(max_mem+1):
		for index in range((1 if length == 0 else 0), len(message)-length):
			substr = message[index:index+length]
			next = message[index+length]
			if substr not in cond_freq:
				cond_freq[substr] = {}
			if (next,) not in cond_freq[substr]:
				cond_freq[substr][(next,)] = 1
			else:
				cond_freq[substr][(next,)] += 1
	
	return cond_freq

##############################################################
################## Message Frequency Logger ##################
##############################################################
#### Category: Core Function
# Uses countMessageFreq to count the conditional probabilities
#	of the message. Then, it uses updateFreq for each
#	conditional string to incorporate the conditional 
#	character counts into each respective conditional
#	character probability file.

def logMessageFreq(message, func_ReadWrite):
	cond_freq = countMessageFreq(message)
	
	# Update/Create probability profile for each conditional string
	for cond in cond_freq:
		tmp = cond_char2code(cond)
		filename = makefilename(tmp if tmp else code_default)
		updateFreq(filename, func_ReadWrite, cond_freq[cond])

##############################################################
###################### Frequency Getter ######################
##############################################################
#### Category: Core Function
# Reads the conditional frequency from data files on disk in
#	the local directory. Returns a dictionary of the
#	conditional probabilities.
def getCondFreq(cond, func_ReadWrite):
	code = (cond_char2code(cond) if cond else code_default)
	
	# Initializes probability dictionary to zero prob.'s
	new_dict = { (char,):0 for char in char_order }
	tmp_dict = None
	while True:
		weight = 1-sum(new_dict.values())
		try:
			tmp_dict = func_ReadWrite[0](makefilename(code))
		except IOError as e:
			# Check file existence (non-existence is NOT fatal)
			if e.errno == errno.ENOENT:
				print 'could not find file: ' + makefilename(code)
			else:
				raise e
		
		for elmt in tmp_dict:
			if elmt in new_dict:
				new_dict[elmt] += tmp_dict[elmt] * weight
			else:
				new_dict[elmt]  = tmp_dict[elmt] * weight
		
		if code == code_default:
			break
		else:
			code = (code[code_unit:] if len(code)<=code_unit else code_default)
	
	return new_dict

