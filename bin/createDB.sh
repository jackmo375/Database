#!/bin/bash

source ./config.sh
source ./secret.sh  # imports: db_user, db_user_pswd

mysql -u ${db_user} -p${db_user_pswd} < ${sql}createDB.sql
