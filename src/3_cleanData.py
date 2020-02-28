#
#	SICKLE IN AFRICA
#	automatic data transfer protocol
#
#	pipeline step 3: data cleaning
#
#######################################

import sys
import argparse

def main():

	inbname   = 'raw' 	# input file base name
	outbname  = 'clean' # output file base name

	args = getShellArguments()

	# import raw data
	infname = args.tempDir + inbname + '.csv'	# input file name
	print(infname)
	infstream = open(infname, 'r')	# input file stream


	# catch missing values

	# ...

	# output cleaned file


#
#  Functions
#

def getShellArguments():
	'''
	Get shell enviroment arguments
	'''
	parser = argparse.ArgumentParser()

	parser.add_argument(
		'--tempDir', 
		type=str, 
		help='path to temporary data storage directory')
	parser.add_argument(
		'--repDir',
		type=str,
		help='path to temporary quality reports storage directory')

	return parser.parse_args()


#
#  Boilerplate
#
if __name__ == '__main__':
	main()