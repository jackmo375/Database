#
#	SickleInAfrica Data quality
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
	args :: all arguments passed to the python 
		script from the bash wrapper.

Each function:
+ performs a set of data quality checks, 
+ saves	the results in the summary_info object
+ performs cleaning by modifying the data set inplace.

'''
import pandas as pd
import datetime

# Local modules:
import dataElements
import cleaningReport

def completeness(data, summary_info, args):
	'''
	Completeness metric

	Description: Are all the core SCD data (SPARCo-base) values available?
	Concrete measure: Provide the number of the SPARCo-base data elements collected
	@params:
		data (pandas dataframe) :: input data pulled from REDCap repository
		summary_info (QualityChecklist object) :: contains all summary info to go into reports
		args (argparse object): arguments passed down from the shell. 
	'''

	summary_info.elements_collected = data.columns


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

	summary_info.n_std_elements = len(set(data.columns).intersection(dataElements.SIA_STD_ELEMENTS))
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
	#is_valid_age = (data['age_at_enrollment'] > 0) & (data['age_at_enrollment'] < args.maxAge)
	#print(data[is_valid_age])


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
	# duplicates
	duplicatedRows = data[data.duplicated()]
	summary_info.n_duplicates = len(duplicatedRows)
	data.drop_duplicates(keep='first', inplace=True)

	# invalid dates
	if 'year_of_diagnosis' in data.columns:
		data_notNull = data[data.year_of_diagnosis.notnull()]
		summary_info.invalid_years = data_notNull[(data_notNull.year_of_diagnosis.astype(int) < 0) | (data_notNull.year_of_diagnosis.astype(int) > datetime.datetime.now().year)][['record_id', 'year_of_diagnosis']]
		summary_info.invalid_years['rejected_field'] = 'year_of_diagnosis'
		summary_info.df_records_removed = summary_info.df_records_removed.append(summary_info.invalid_years[['record_id', 'rejected_field']])
	
	# invalid ages
	if 'age_at_today' in data.columns:
		data_notNull = data[data.age_at_today.notnull()]
		summary_info.invalid_age_at_today = data_notNull[(data_notNull.age_at_today.astype(int) < 0) | (data_notNull.age_at_today.astype(int) > args.maxAge)][['record_id', 'age_at_today']]
		summary_info.invalid_age_at_today['rejected_field'] = 'age_at_today'
		summary_info.df_records_removed = summary_info.df_records_removed.append(summary_info.invalid_age_at_today[['record_id', 'rejected_field']])

	if 'age_at_enrollment' in data.columns:
		data_notNull = data[data.age_at_enrollment.notnull()]
		summary_info.invalid_age_at_enrol = data_notNull[(data_notNull.age_at_enrollment.astype(int) < 0) | (data_notNull.age_at_enrollment.astype(int) > args.maxAge)][['record_id', 'age_at_enrollment']]		
		summary_info.invalid_age_at_enrol['rejected_field'] = 'age_at_enrollment'
		summary_info.df_records_removed = summary_info.df_records_removed.append(summary_info.invalid_age_at_enrol[['record_id', 'rejected_field']])

		if 'age_at_today' in data.columns:
			data_notNull = data[(data.age_at_enrollment.notnull()) & (data.age_at_today.notnull())]
			summary_info.conflicting_ages = data_notNull[data_notNull.age_at_enrollment.astype(int) > data_notNull.age_at_today.astype(int)][['record_id', 'age_at_enrollment', 'age_at_today']]
			summary_info.conflicting_ages['rejected_field'] = 'age_at_today WITH age_at_enrollment'
			summary_info.df_records_removed = summary_info.df_records_removed.append(summary_info.conflicting_ages[['record_id', 'rejected_field']])


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
	summary_info.missing_values = data.isnull().sum()

	collected_base_elements = list(set(data.columns) & set(dataElements.SIA_BASE_ELEMENTS))
	summary_info.missing_base_values = data[collected_base_elements].isnull().sum()
