#!/usr/bin/env python

"""
This python code builds and updates the database of SCD patients Recruited in the context of SADaCC and SPARCo projects.
This program has been written by Gaston K. Mazandu <gmazandu@gmail.com, kuzamunu@aims.ac.za, gaston.mazandu@uct.ac.za, 
Copyright (2018) SADaCC/UCT under free software (GNU General Public Licence). 
All rights reserved.
"""

import sys, os, re, subprocess, argparse
import stat, time
import pandas as pd

from datetime import timedelta, date

__all__ = []
__author__ = """Gaston K. Mazandu (gmazandu@gmail.com, kuzamunu@aims.ac.za, gaston.mazandu@uct.ac.za)"""


def main():

	args = getShellArguments()

	outLabel  = 'raw' # output file label

	# Calling datasets from SPARCo sites here
	data = subprocess.check_output(
		["/bin/sh", 
		"-c", 
		"php "
			+ args.srcDir
			+ "php/callsparcodata.php "
			+ args.siteURL + " "
			+ args.apiURL  + " "
			+ args.apiTok
			+ "; exit 0"]) # Calling datasets here

	# Processing datasets	
	Data = {}; Elements = set()
	for line in data.decode().split('<br/>'):
		if not line.strip(): continue
		tline = [s.strip() for s in line.split('s_@@_@$_$$_p')]
		Data[tline[0]] = eval(tline[1]); Data[tline[0]]['country'] = 'tz'
		Elements |= set(Data[tline[0]].keys())

	df = pd.DataFrame.from_dict(Data, orient='index', dtype=object)
	df.set_index('record_id', inplace=True)

	# save as csv file for cleaning:
	outName = args.tempDir + outLabel + '.csv' # output file name
	df.to_csv(outName)

	print(df.head())
	print("Number of data fields in incoming data: " + str(len(Elements)))


def ttype(s):
	try: return type(eval(s))
	except: return type(s)


def getShellArguments():
	'''
	Get shell enviroment arguments
	'''
	parser = argparse.ArgumentParser()

	parser.add_argument(
		'--srcDir',
		type=str,
		help='path to source code directory')
	parser.add_argument(
		'--tempDir', 
		type=str, 
		help='path to temporary data storage directory')
	parser.add_argument(
		'--siteURL', 
		type=str, 
		help='redcap site hosting the data')
	parser.add_argument(
		'--apiURL', 
		type=str, 
		help='REDCap API url')
	parser.add_argument(
		'--apiTok', 
		type=str, 
		help='key to access REDCap API')

	return parser.parse_args()


if __name__=='__main__':
	main()