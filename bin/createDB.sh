#!/bin/bash

source ./config.sh
source ./secret.sh  # imports: mariadb_jack

mysql -u ${user} -p${user_pswd} < ${sql}createDB.sql
