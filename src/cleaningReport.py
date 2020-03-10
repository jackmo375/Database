#
#	Checklist class
#
#####################

import pandas as pd

# local modules:
import dataElements

class Report:
	def __init__(self):

		self.df_records_removed = pd.DataFrame(columns=['record_id', 'rejected_field'])


	def n_elements_collected(self):
		'''
		returns total number of data elements 
		downoaded from REDCap server
		'''
		return len(self.elements_collected)

	def n_base_elements_collected(self):
		'''
		returns total number of data elements 
		downloaded from REDCap server that
		are approved as SickleInAfrica *base* 
		elements
		'''
		return len(set(self.elements_collected).intersection(dataElements.SIA_BASE_ELEMENTS))

	def n_std_elements_collected(self):
		'''
		returns total number of data elements 
		downloaded from REDCap server that
		are approved as SickleInAfrica 
		standardized elements
		'''
		return len(set(self.elements_collected).intersection(dataElements.SIA_STD_ELEMENTS))


	def write_long_report(self, fname):
		'''
		write full cleaning report to send back to the data source. 
		Includes information on any subsets of the raw data that
		did not pass cleaning checks.
		'''

		report_str = ''

		# Completeness:
		report_str = report_str \
			+ '+ Summary of data collection:\n' \
			+ "SIA base elements           {}\n".format(len(dataElements.SIA_BASE_ELEMENTS)) \
			+ "SIA standardized elements   {}\n".format(len(dataElements.SIA_STD_ELEMENTS)) \
			+ "data elements collected     {}\n".format(self.n_elements_collected()) \
			+ "*base* elements collected   {}\n".format(self.n_base_elements_collected()) \
			+ "standard elements collected {}\n".format(self.n_std_elements_collected()) \
			+ "**Note** some of the standardized elements have been removed for de-identification.\n"
		report_str += '\n'

		# Consistency:
		report_str += "duplicates {}\n".format(self.n_duplicates)
		report_str += '\n'

		report_str += quality_check_to_string(
			'year_of_diagnosis', 
			self.elements_collected,
			self.invalid_years)

		report_str += quality_check_to_string(
			'age_at_today',
			self.elements_collected,
			self.invalid_age_at_today)

		report_str += quality_check_to_string(
			'age_at_enrollment',
			self.elements_collected,
			self.invalid_age_at_enrol)

		report_str += quality_check_to_string(
			['age_at_enrollment', 'age_at_today'],
			self.elements_collected,
			self.conflicting_ages)

		# Missing values:
		print('+ Missing base values:')
		print(self.missing_base_values)
		print()

		# Records rejected after cleaning:
		print("+ Records rejected after cleaning:")
		print(self.df_records_removed)

		print(report_str)


	def write_short_report(self, fname):
		'''
		Write short summary report of the cleaning process,
		to brief collaberation members on the database update.

		Output format should be html, and <fname> should have
		the correct '.htm' extension. 
		'''

		outStream = open(fname, 'w')

		# write report here....

		outStream.close()


def quality_check_to_string(field, element_list, df):

	return_str = ''

	if isinstance(field, list) is False:
		if field in element_list:
			return_str += "+ Records found with invalid "+field+" values:\n"
			if df.empty is False:
				return_str += str(df) + '\n'
			else:
				return_str += 'None\n'
		else:
			return_str += field+' field not recorded\n'
		return_str += '\n'
	else:
		if field[0] in element_list and field[1] in element_list:
			return_str += "+ Records found with conflicting "+field[0]+", "+field[1]+" values:\n"
			if df.empty is False:
				return_str += str(df) + '\n'
			else:
				return_str += 'None\n'
		else:
			return_str += field[0]+', '+field[1]+' fields not recorded together\n'
		return_str += '\n'

	return return_str


def create_empty_report():
	''''
	Report class constructor:

	creates an empty Report object
	'''
	return Report()