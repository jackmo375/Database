#
#	SICKLE IN AFRICA
#	automatic data transfer protocol
#
#	pipeline step 4: converting clean data to SQL 
#	format, including any data normalisation.
#
######################################################

import csv, argparse

# Local modules
import dataElements

def main():

	flabel = 'clean'

	args = getShellArguments()

	infname  = args.tempDir + flabel + '.csv'

	sql_outStream = openSQLfile(flabel, args)

	# read in cleaned data:
	with open(infname) as csv_file:
		csv_reader = csv.reader(csv_file, delimiter=',')

		# get file headers
		headers = next(csv_reader)
		# the python csv writer inserts a row number column at the start
		# with a blank column name, so we must correct for this:
		if headers[0] == '':
			headers[0] = '#'

		sql_outStream.write(
			  'INSERT INTO main\n'
			+ 'VALUES\n')

		row = next(csv_reader)
		value_string = '\t('
		for j, field in enumerate(headers):
			if field in dataElements.SIA_BASE_ELEMENTS:
				if row[j] is not None:
					value_string = value_string + row[j] + ','
				else:
					value_string = value_string + 'NULL' + ','
		value_string = value_string[0:-1] + ')'
		sql_outStream.write(value_string)

		# read data
		for i, row in enumerate(csv_reader):

			value_string = ',\n\t('

			for j, field in enumerate(headers):
				if field in dataElements.SIA_BASE_ELEMENTS:
					if row[j] != '':
						value_string = value_string + row[j] + ','
					else:
						value_string = value_string + 'NULL' + ','

			value_string = value_string[0:-1] + ')'

			sql_outStream.write(value_string)

		sql_outStream.write(';')


	csv_file.close()
	sql_outStream.close()


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
		'--dbName',
		type=str,
		help='name of target SQL database')

	return parser.parse_args()


def openSQLfile(flabel, args):

	outfname = args.tempDir + flabel + '.sql'
	outStream = open(outfname, 'w')
	outStream.write(
		  '--\n'
		+ '--    REDCap data to be added to SQL database\n'
		+ '--\n'
		+ '---------------------------------------------\n'
		+ '\n'
		+ 'USE ' + args.dbName + ';\n')

	return outStream



if __name__ == '__main__':
	main()