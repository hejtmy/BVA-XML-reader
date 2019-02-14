import sys
## The command needs to be in the following format
# path to hte file originates in the active directory
# path is specified using double quotes and os.sensitive separator (win: \, unix: /)
# Example: python xml_to_csv.py "example_data\example.xml"

import os

import matplotlib.pyplot as plt
from functions.bva_xml_reader import read_xml_bva
from functions.bva_xml_reader import save_csv

## Validations
if (len(sys.argv) < 2):
	sys.exit('You have to provide xml input file')
else:
	#TODO - issue with comman with single instead of double quotes
	path = os.getcwd() + '\\' + sys.argv[1]

if (len(sys.argv) < 3):
	print('output file will be output.csv')
	output = 'output.csv'
else:
	output = sys.argv[2]

pd_bva = read_xml_bva(path)
save_csv(pd_bva, output)