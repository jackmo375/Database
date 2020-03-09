#
#  test step 2.
#  cleaning the raw data
#
###################################

#!/bin/bash

source ../bin/config.sh
source ../bin/secret.sh	# imports: site_url, api_url, api_token, db_user, db_user_pswd

#
#	Pipeline
#

# enter python virtual enviroment
source ${pve}bin/activate

# 2. clean data
echo 'Cleaning raw data...'
python3 ${src}2_cleanData.py \
	--tempDir ${dat} \
	--repDir  ${rep} \
	--maxAge  ${maxAge} && echo '...done.'

# exit python virtual enviroment
deactivate