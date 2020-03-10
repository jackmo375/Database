#
#	SICKLE IN AFRICA
#	automatic data transfer protocol
#
#######################################
#######################################

#!/bin/bash

source ./config.sh
source ./secret.sh	# imports: site_url, api_url, api_token, db_user, db_user_pswd

#
#	Pipeline
#

# enter python virtual enviroment
source ${pve}bin/activate

# 1. download REDCap data elements:
echo 'Downloading REDCap data elements...'
python3 ${src}1_pullFromREDCap.py \
	--srcDir  ${src} \
	--tempDir ${dat} \
	--siteURL ${site_url} \
	--apiURL  ${api_url} \
	--apiTok  ${api_token} && echo '...done.'

# 2. clean data
echo 'Cleaning raw data...'
python3 ${src}2_cleanData.py \
	--tempDir ${dat} \
	--repDir  ${rep} \
	--maxAge  ${maxAge} && echo '...done.'

# 3. convert clean data to SQL (including normalisation) and upload to database
echo "Uploading clean data to database..."
python3 ${src}3_convertToSQL.py  \
	--tempDir ${dat} \
	--repDir  ${rep} \
	--dbName  ${dbName} \
	--dbUser  ${db_user} \
	--dbPswd  ${db_user_pswd} && echo "...done."

# 5. distribute quality reports

# exit python virtual enviroment
deactivate

# clean temporary files
