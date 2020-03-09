<?php
/*
Author: Gaston Mazandu

This python code builds and updates the database of SCD patients Recruited in the context of SADaCC and SPARCo projects.
This program has been written by Gaston K. Mazandu <gmazandu@gmail.com, kuzamunu@aims.ac.za, gaston.mazandu@uct.ac.za, 
Copyright (2018) SADaCC/UCT under free software (GNU General Public Licence). 
All rights reserved.
*/

$site_url  = $argv[1];
$api_url   = $argv[2];
$api_token = $argv[3];

include 'RestCallRequest.php';

session_start(); // Starting Session

$now = time();
if (isset($_SESSION['discard_after']) && $now > $_SESSION['discard_after']) {
	// this session has worn out its welcome; kill it and start a brand new one
	session_unset();
	session_destroy();
	session_start();
}



