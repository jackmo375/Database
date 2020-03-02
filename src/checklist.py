#
#	Checklist class
#
#####################

#
#  Class defintion
#
class Checklist:
	# SickleInAfrica base data elements
	SIA_BASE_ELEMENTS = [
		'age_at_enrollment',
		'age_at_today',
		'marital_status',
		'sex',
		'year_of_diagnosis'
	]
	# SickleInAfrica standard data elements
	SIA_STD_ELEMENTS = SIA_BASE_ELEMENTS + [
		'scd_test_result_ss_sbthal'
	]

	def __init__(
			self,
			n_base_elements,
			n_std_elements,
			n_elements,
			n_duplicates, 
			n_missing_values,
			frac_missing,
			n_records_removed):
		self.n_base_elements = n_base_elements
		self.n_std_elements = n_std_elements
		self.n_elements = n_elements
		self.n_duplicates = n_duplicates
		self.n_missing_values = n_missing_values
		self.frac_missing = frac_missing
		self.n_records_removed = n_records_removed


	def write_long_report(self, fname):
		'''
		write full cleaning report to send back to the data source. 
		Includes information on any subsets of the raw data that
		did not pass cleaning checks.

		Output file format should be .md (markdown), and <fname> should 
		have the correct '.md' extension.   
		'''
		outStream = open(fname, 'w')
		outStream.write(
			'SADaCC Data Cleaning full report\n' +
			'================================\n')

		outStream.write(
			'number of base data elements collected: ' 
			+ str(self.n_base_elements) + '\n')
		outStream.write(
			'number of standard data elements collected: ' 
			+ str(self.n_std_elements) + '\n')
		outStream.write(
			'number of unique records removed: '
			+ str(self.n_records_removed) + '\n')
		outStream.write(
			'# Validity\n'
			+ 'standard elements / total elements collected: ' 
			+ str(self.n_std_elements/self.n_elements) + '\n')
		outStream.write(
			'# Consistency\n'
			+ 'number of duplicates removed: '
			+ str(self.n_duplicates) + '\n')
		outStream.write(
			'# Missing Values\n'
			+ 'mumber of missing values: '
			+ str(self.n_missing_values) + '\n'
			+ 'fraction of values missing: '
			+ str(self.frac_missing) + '\n')

		outStream.close()


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

#
#  Constructors
#
def create_empty_checklist():

	return Checklist(0,0,0,0,0,0,0)