#
#	SICKLE IN AFRICA
#	automatic data transfer protocol
#
#	pipeline step 3: data cleaning
#
#######################################

import sys
import argparse
import pandas as pd

import dataQuality, checklist

def main():

	inbname   = 'raw' 	# input file base name
	outbname  = 'clean' # output file base name

	args = getShellArguments()

	# import raw data
	infname = args.tempDir + inbname + '.csv'	# input file name
	data = pd.read_csv(infname)					# import as pandas dataframe

	# initialize summary object
	summary_info = checklist.create_empty_checklist()

	# -PERFORMING QUALITY CHECKS-
	
	dataQuality.completeness(data, summary_info, args)

	dataQuality.validity(data, summary_info, args)

	dataQuality.integrability(data, summary_info, args)

	dataQuality.integrity(data, summary_info, args)

	dataQuality.accuracy(data, summary_info, args)

	dataQuality.consistency(data, summary_info, args)

	dataQuality.timeliness(data, summary_info, args)

	dataQuality.missingValues(data, summary_info, args)

	# -END OF QUALITY CHECKS-

	# print data cleaning summary reports

	summary_info.write_long_report(args.repDir + 'cleaningReport.long.md')

	# output cleaned file
	outfname = args.tempDir + outbname + '.csv' # output file name
	data.to_csv(outfname)


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