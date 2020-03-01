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
	SIA_STD_ELEMENTS = SIA_BASE_ELEMENTS + [] 

	def __init__(
			self,
			n_base_elements,
			n_std_elements,
			n_elements):
		self.n_base_elements = n_base_elements
		self.n_std_elements = n_std_elements
		self.n_elements = n_elements


def create_empty_checklist():

	return Checklist(0,0,0)


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

	Description:
	Concrete measure:

	'''
	pass

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

	Description:
	Concrete measure:

	'''
	pass


def timeliness(data, summary_info, args):
	'''
	Integrity metric

	Description:
	Concrete measure:

	'''
	pass