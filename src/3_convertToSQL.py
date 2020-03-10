#
#	SICKLE IN AFRICA
#	automatic data transfer protocol
#
#	pipeline step 4: converting clean data to SQL 
#	format, including any data normalisation.
#
######################################################

import csv, argparse
import pandas as pd
import sqlalchemy as db

# Local modules
import dataElements

def main():

	flabel = 'clean'

	args = getShellArguments()

	# import raw data
	infname  = args.tempDir + flabel + '.csv'
	data = pd.read_csv(infname, dtype=object)	# import as pandas dataframe
	data.set_index('record_id')

	engine = db.create_engine(
		'mysql+pymysql://'
		+ args.dbUser
		+ ':'
		+ args.dbPswd
		+ '@localhost/'
		+ args.dbName, 
		echo=True)

	collected_base_elements = list(set(data.columns) & set(dataElements.SIA_BASE_ELEMENTS))

	data[collected_base_elements].to_sql('base', con=engine, if_exists='replace')	# 'base' is the target database table name. 


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
	parser.add_argument(
		'--dbUser',
		type=str,
		help='name of target SQL database user')
	parser.add_argument(
		'--dbPswd',
		type=str,
		help='name of target SQL database user password')

	return parser.parse_args()


if __name__ == '__main__':
	main()