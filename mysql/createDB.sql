--Create a Sickle In Africa SQL database 

CREATE DATABASE IF NOT EXISTS sia;

USE sia;
CREATE TABLE IF NOT EXISTS main (
	age_at_enrollment int,
	age_at_today int,
	marital_status int,
	sex int,
	year_of_diagnosis int,
	scd_test_result_ss_sbthal int
);

SHOW Databases;
SHOW Tables;