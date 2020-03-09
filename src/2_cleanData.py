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

# Local modules:
import dataElements
import dataQuality
import cleaningReport


def main():

	inbname   = 'raw' 	# input file base name
	outbname  = 'clean' # output file base name

	args = getShellArguments()

	# import raw data
	infname = args.tempDir + inbname + '.csv'	# input file name
	data = pd.read_csv(infname, dtype=object)	# import as pandas dataframe
	data.set_index('record_id')

	# initialize summary object
	summary_info = cleaningReport.create_empty_report()

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

	print("Records rejected after cleaning:")
	print(summary_info.df_records_removed)

	summary_info.write_long_report(args.repDir + 'cleaningReport.long.md')

	# output cleaned file
	outfname = args.tempDir + outbname + '.csv' # output file name
	data.to_csv(outfname, index=False)


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
	parser.add_argument(
		'--maxAge',
		type=int,
		help='maximum plausible age of a patient')

	return parser.parse_args()


if __name__ == '__main__':
	main()