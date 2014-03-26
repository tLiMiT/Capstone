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

char_order = ['\n', ' ', '!', '"', '#', '$', '%', '&', "'", 
	'(', ')', '*', '+', ',', '-', '.', '/', '0', '1', '2', 
	'3', '4', '5', '6', '7', '8', '9', ':', ';', '<', '=', 
	'>', '?', '@', 'C', '[', '\\', ']', '^', '_', '`', 'a', 
	'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 
	'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 
	'x', 'y', 'z', '{', '|', '}', '~']


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
# Legible to Escape - str.encode('string_escape')

##############################################################
#################### Frequency File Updater ##################
##############################################################
# dict_freq - a dictionary list
#	keys - letters observed in message
#	values - number of occurences in messages (NOT %)
def updateFreq(filename, func_ReadWrite, dict_freq):
	old_dict = {}
	try:
		old_dict = func_ReadWrite[0](filename)
	except IOError as e:
		# Check file existence
		if e.errno == errno.ENOENT:
			pass
		else:
			raise e
	
	size1 = sum(dict_freq.values())
	size2 = half_life
	
	new_dict = {}
	for char in char_order:
		new_dict[(char,)] = 0
		if (char,) in dict_freq:
			new_dict[(char,)] += dict_freq[(char,)] * (1.0 / (size1+size2))
		if (char,) in old_dict:
			new_dict[(char,)] += old_dict[(char,)] * (size2 / (size1+size2))

	for cntr in range(2):
		func_ReadWrite[1](filename, new_dict)
		test = func_ReadWrite[0](filename)
		if test == new_dict:
			break
		elif cntr == 1:
			print 'Error: write to binary failed'

def logMessageFreq(message, func_ReadWrite):
	# Pre-analysis formatting
	message = '\x02' + message
	# TODO - accomodate caps setting
	
	cond_freq = {}
	for length in range(max_mem+1):
		for index in range((1 if length == 0 else 0), len(message)-length):
			substr = message[index:index+length]
			next = message[index+length]
			if substr not in cond_freq:
				cond_freq[substr] = {}
			if (next,) not in cond_freq[substr]:
				cond_freq[substr][(next,)] = 0
			cond_freq[substr][(next,)] += 1
	
	# Update/Create probability profile for each conditional string
	for cond in cond_freq:
		tmp = [str(ord(sub)) for sub in cond]
		tmp = [ '0'*(3-len(s)) + s for s in tmp]
		filename = bin_prefix \
			+ (''.join(tmp) if tmp else code_default) \
			+ bin_extension
		updateFreq(filename, func_ReadWrite, cond_freq[cond])

def getCondFreq(cond, func_ReadWrite):
	code = None
	if len(cond) == 0:
		code = code_default
	else:
		tmp = [str(ord(sub)) for sub in cond]
		tmp = [ '0'*(3-len(s)) + s for s in tmp]
		code = ''.join(tmp)
	
	new_dict = { (char,):0 for char in char_order }
	tmp_dict = None
	while True:
		weight = 1-sum(new_dict.values())
		try:
			tmp_dict = func_ReadWrite[0](makefilename(code))
		except IOError as e:
			# Check file existence
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
			code = (code[3:] if len(code)<=3 else code_default)
	
	return new_dict

