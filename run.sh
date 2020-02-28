#
#	SICKLE IN AFRICA
#	automatic data transfer protocol
#
#######################################
#######################################

#!/bin/bash

source ./config.sh

#
#	Pipeline
#

# 1. send data request to REDCap

# 2. download raw data

# 3. clean data
python ${src}3_cleanData.py \
	--tempDir ${dat} \
	--repDir ${rep}

# 4. convert clean data to SQL format

# 5. send clean data to SIA database

# 6. distribute quality reports
