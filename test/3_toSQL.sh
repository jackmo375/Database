#
#  test step 3
#  converting csv data to mySQL
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

# 3. convert clean data to SQL format (including normalisation)
echo "Converting cleaned data to SQL format (including normalisation)..."
python3 ${src}3_convertToSQL.py  \
	--tempDir ${dat} \
	--repDir  ${rep} \
	--dbName  ${dbName} \
	--dbUser  ${db_user} \
	--dbPswd  ${db_user_pswd} || { echo '...failed!'; exit 1; } && echo '...done.'

# exit python virtual enviroment
deactivate