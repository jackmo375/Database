#
#	SADaCC Data quality module
#
#################################
'''
The general idea behind this module is that
it is a list of functions, each addressing a 
different dimension of data quality. 

All functions in this module take as input:
	data :: a dataframe containing the pulled data
	summary_info :: a Checklist object containing
		all info on the data cleaning process
	args :: a ll arguments passed to the python 
		script from the bash wrapper.

Each function:
+ performs a set of data quality checks, 
+ saves	the results in the summary_info object
+ performs cleaning by modifying the data set inplace.

'''

def completeness(data, summary_info, args):
	'''
	Completeness metric

	Description: Are all the core SCD  data (SPARCo-base) values available?
	Concrete measure: Provide the number of the SPARCo-base data elements collected
	@params:
		data (pandas dataframe) :: input data pulled from REDCap repository
		summary_info (QualityChecklist object) :: contains all summary info to go into reports
		args (argparse object): arguments passed down from the shell. 
	'''

	summary_info.n_base_elements = len(set(data.columns).intersection(summary_info.SIA_BASE_ELEMENTS))


def validity(data, summary_info, args):
	'''
	Validity metric

	Description: Are all data values collected using the standardized SCD data elements?
	Concrete measure: Provide the number of overall collected data elements as compared 
		to Standardized data element set
	@params:
		data (pandas dataframe) :: input data pulled from REDCap repository
		summary_info (QualityChecklist object) :: contains all summary info to go into reports
		args (argparse object): arguments passed down from the shell. 
	'''

	summary_info.n_std_elements = len(set(data.columns).intersection(summary_info.SIA_STD_ELEMENTS))
	summary_info.n_elements = len(data.columns)

	# then validity is just n_std_elements/n_elements


def integrability(data, summary_info, args):
	'''
	Integrability metric

	Description: is the data easily shareable, use the same measures
	Concrete  measure:
	@params:

	'''
	pass


def integrity(data, summary_info, args):
	'''
	Integrity metric

	Description: Are the relations between entities and attributes consistent
	Concrete measure: Provide the number of data elements consistent with its value or content

	'''
	# SIA Base elements:
	is_valid_age = (data['age_at_enrollment'] > 0) & (data['age_at_enrollment'] < args.maxAge)
	print(data[is_valid_age])


def accuracy(data, summary_info, args):
	'''
	Accuracy metric

	Description:
	Concrete measure:

	'''
	pass


def consistency(data, summary_info, args):
	'''
	Consistency metric

	Description: Are there duplicate records? (Redundancy checks)
	Concrete measure: Provide the number of duplicated records detected

	'''
	duplicatedRows = data[data.duplicated()]
	summary_info.n_duplicates = len(duplicatedRows)
	data.drop_duplicates(keep='first', inplace=True)


def timeliness(data, summary_info, args):
	'''
	timeless metric

	Description: Is data available for transfer to the central database in a timely manner?
	Concrete measure: Provide the quantity of records transferred with respect to indicators

	'''
	pass


def missingValues(data, summary_info, args):
	'''
	Summarise the missing values in the input raw data file
	'''
	# number of values missing:
	summary_info.n_missing_values = data.isnull().sum().sum()
	summary_info.frac_missing \
		= summary_info.n_missing_values / (len(data.columns) * len(data))