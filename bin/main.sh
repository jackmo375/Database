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

# 1. check REDCap data elements:
python3 ${src}1_checkdataelement.py \
	--srcDir  ${src} \
	--tempDir ${dat} \
	--siteURL ${site_url} \
	--apiURL  ${api_url} \
	--apiTok  ${api_token}

# 2. download raw data to temp location

# 3. clean data
python3 ${src}3_cleanData.py \
	--tempDir ${dat} \
	--repDir  ${rep} \
	--maxAge  ${maxAge}

# 4. convert clean data to SQL format (including normalisation)
python3 ${src}4_convertToSQL.py  \
	--tempDir ${dat} \
	--repDir  ${rep} \
	--dbName  ${dbName}

# 5. send clean data to SIA database
mysql -u ${db_user} -p${db_user_pswd} < ${dat}clean.sql

# 6. distribute quality reports

# exit python virtual enviroment
deactivate

# clean temporary files
