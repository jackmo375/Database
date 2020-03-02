#!/bin/bash

./dropDB.sh
./createDB.sh
./main.sh
mysql -u jack -parchi3 sia -e 'SELECT * FROM main'