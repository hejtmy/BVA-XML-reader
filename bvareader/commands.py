import sys
import os
from bvareader.reader import read_xml_bva
from bvareader.reader import save_csv
from bvareader.preprocessing import add_rotation
from bvareader.preprocessing import preprocess_bva_data

## The command needs to be in the following format
# path to the file originates in the active directory: path is specified using double quotes and os.sensitive separator (win: \, unix: /)
# Name of the output file without extension
# Example: python xml_to_csv.py "example_data\example.xml" "output"
def bva_preprocess_xml():

    ## Validations
    if (len(sys.argv) < 2):
        sys.exit('You have to provide xml input file')
    else:
        #TODO - issue with comman with single instead of double quotes
        path = os.getcwd() + '\\' + sys.argv[1]

    if (len(sys.argv) < 3):
        print('output file will be output.csv')
        output = 'output'
    else:
        output = sys.argv[2]

    pd_bva = read_xml_bva(path)
    pd_bva = add_rotation(pd_bva)
    pd_bva2 = preprocess_bva_data(pd_bva)

    save_csv(pd_bva, output + '_full.csv')
    save_csv(pd_bva2, output + '.csv')