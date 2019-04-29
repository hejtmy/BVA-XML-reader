import sys
import os
from bvareader import reader
from bvareader.preprocessing import add_rotation
from bvareader.preprocessing import preprocess_bva_data


#' The command needs to be in the following format:
#' path to the file originates in the active directory: path is specified using double quotes and os.sensitive separator (win: \, unix: /)
#' Name of the output file without extension
#' Example: python xml_to_csv.py "example_data\example.xml" "output"
def bva_preprocess_xml():
    # Validations
    path = get_sys_filepath(sys.argv)

    output_name = default_sys_argument(sys.argv, 'bva_output')

    pd_bva = reader.read_xml_bva(path)
    pd_bva = add_rotation(pd_bva)
    pd_bva2 = preprocess_bva_data(pd_bva)

    reader.save_csv(pd_bva, output + '_full.csv')
    reader.save_csv(pd_bva2, output + '.csv')


def bva_get_sync_times():
     # Validations
    path = get_sys_filepath(sys.argv)
    output_name = default_sys_argument(sys.argv, 'sync')



def bva_get_phases_table():
    # Validations
    path = get_sys_filepath(sys.argv)
    output_name = default_sys_argument(sys.argv, 'phases2')
    pd_phases = reader.read_xml_phases(path)
    reader.save_csv(pd_phases, output_name + '.csv')


def xml_settings_to_csv():
        # Validations
    if (len(sys.argv) < 2):
        sys.exit('You have to provide xml input file')
    else:
        # TODO - issue with comman with single instead of double quotes
        path = os.getcwd() + '\\' + sys.argv[1]

    if (len(sys.argv) < 3):
        print('output file will be settings.csv')
        output = 'settings'
    else:
        output = sys.argv[2]

    pd_settings = reader.read_xml_settings(path)

    reader.save_csv(pd_settings, output + '.csv')


def get_sys_filepath(args):
    if (len(args) < 2):
        sys.exit('You have to provide valid input file path')
    else:
        # TODO - issue with comman with single instead of double quotes
        path = os.getcwd() + '\\' + args[1]
        # check existence
    return(path)

def default_sys_argument(args, default):
    if (len(args) < 3): 
        output_name = default
    else:
        output_name = args[2]
    print('output file will be named ' + output_name + '.csv')
    return(output_name)
