#
#	test step 4.
#	email data cleaning reports
#
##################################

#!/bin/bash

source ../bin/config.sh
source ../bin/secret.sh	# imports: site_url, api_url, api_token, db_user, db_user_pswd

#
#	Pipeline
#

# enter python virtual enviroment
source ${pve}bin/activate

# 4. distribute quality reports
echo "Emailing data cleaning reports..."
python3 ${src}4_emailReports.py \
	--repDir   ${rep} \
	--fromAdd  ${from_add} \
	--fromPswd ${from_add_pswd} \
	--toAdd    ${to_add} && echo "...done."

# exit python virtual enviroment
deactivate