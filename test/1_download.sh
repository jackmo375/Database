#
#  test step 1.
#  downloading REDCap data
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

# 1. check REDCap data elements:
echo "Downloading REDCap data..."
python3 ${src}1_pullFromREDCap.py \
	--srcDir  ${src} \
	--tempDir ${dat} \
	--siteURL ${site_url} \
	--apiURL  ${api_url} \
	--apiTok  ${api_token} || { echo '...failed!'; exit 1; } && echo '...done.'

# exit python virtual enviroment
deactivate
