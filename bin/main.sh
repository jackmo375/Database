#
#	SICKLE IN AFRICA
#	automatic data transfer protocol
#
#######################################
#######################################

#!/bin/bash

source ./config.sh
source ./secret.sh	# defines ${user}, ${user_pswd}

#
#	Pipeline
#

# enter python virtual enviroment
source ${pve}bin/activate

# 1. send data request to REDCap

# 2. download raw data to temp location

# 3. clean data
python3 ${src}3_cleanData.py \
	--tempDir ${dat} \
	--repDir ${rep} \
	--maxAge ${maxAge}

# 4. convert clean data to SQL format (including normalisation)
python3 ${src}4_convertToSQL.py  \
	--tempDir ${dat} \
	--repDir ${rep} \
	--dbName ${dbName}

# 5. send clean data to SIA database
mysql -u ${user} -p${user_pswd} < ${dat}clean.sql

# 6. distribute quality reports

# exit python virtual enviroment
deactivate

# clean temporary files
