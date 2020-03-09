<?php
/*
Author: Gaston Mazandu

This python code builds and updates the database of SCD patients Recruited in the context of SADaCC and SPARCo projects.
This program has been written by Gaston K. Mazandu <gmazandu@gmail.com, kuzamunu@aims.ac.za, gaston.mazandu@uct.ac.za, 
Copyright (2018) SADaCC/UCT under free software (GNU General Public Licence). 
All rights reserved.
*/

include 'config.php';

// either new or old, it should live at most for another hour
$_SESSION['discard_after'] = $now + 3600;

# check command line arguments passed successfully:
if (isset($argc)) {
  for ($i=0; $i<$argc; $i++) {
    echo "Argument #".$i." - ".$argv[$i]."\n";
  }
}
else {
  echo "argc and argv disabled\n";
}

function export_records($type='flat', $records=array(), $events=array(), $fields=array(), $forms=array()){
	global $api_url, $api_token;
	# an array containing all the elements that must be submitted to the API
	$data = array('content' => 'record', 'type' => $type, 'format' => 'json', 'records' => $records, 'events' => $events,
	              'fields' => $fields, 'forms' => $forms, 'exportSurveyFields'=>'true', 'exportDataAccessGroups'=>'false',
	              'token' => $api_token);

	# create a new API request object
	$request = new RestCallRequest($api_url, 'POST', $data);

	# initiate the API request
	$request->execute();
	$my_records = $request->getResponseBody();
	
	$my_records_json = json_decode($my_records);
	$datas = array();
	foreach ( $my_records_json as $my_record ){// Creating record array
		$datas[ $my_record->record ][ $my_record->field_name ] = $my_record->value;
	}
	return $datas; 
}

$my_records = export_records('eav'); #$type='eav', $records=array(), $events=array(), $fields=array(), $forms=array());


$wholeDataset = '';
foreach ($my_records as $my_record_id => $my_record){
	$tmp = json_encode($my_record);
	$wholeDataset .= $my_record_id.'s_@@_@$_$$_p'.$tmp.'<br/>';
}
echo $wholeDataset;
session_destroy();

