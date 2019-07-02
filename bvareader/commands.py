import sys
import os
from bvareader import reader
from bvareader.preprocessing import add_rotation
from bvareader.preprocessing import preprocess_bva_data


# ' The command needs to be in the following format:
# ' path to the file originating in the active directory, using double quotes and os.sensitive separator
# ' Name of the output file without extension, e.g. "patient154"
# '
# ' Example: python xml_to_csv.py "example_data\p154_456.xml" "patient154"


def bva_preprocess_xml():
    # Validations
    path = get_sys_filepath(sys.argv)
    output_path = create_output_path(sys.argv)

    pd_bva = reader.read_xml_bva(path)
    pd_bva = add_rotation(pd_bva)
    pd_bva2 = preprocess_bva_data(pd_bva)
    pd_sync = reader.read_xml_sync(path)
    pd_phases = reader.read_xml_phases(path)
    try:
        pd_start_stop = reader.read_measure_start_stop(path)
        reader.save_csv(pd_start_stop, output_path + 'measure_start_stop.csv')
    except(Exception):
        print("Could not process start and stop due to non appropriate data")
        pass
    reader.save_csv(pd_bva, output_path + 'positions_full.csv')
    reader.save_csv(pd_bva2, output_path + 'positions.csv')
    reader.save_csv(pd_sync, output_path + 'sync_times.csv')
    reader.save_csv(pd_phases, output_path + 'phases.csv')


def bva_positions_table():
    # Validations
    path = get_sys_filepath(sys.argv)
    output_path = create_output_path(sys.argv) + 'positions'

    pd_bva = reader.read_xml_bva(path)
    pd_bva = add_rotation(pd_bva)
    pd_bva2 = preprocess_bva_data(pd_bva)

    reader.save_csv(pd_bva, output_path + '_full.csv')
    reader.save_csv(pd_bva2, output_path + '.csv')


def bva_sync_times_table():
    # Validations
    path = get_sys_filepath(sys.argv)
    output_path = create_output_path(sys.argv) + 'sync_times.csv'
    pd_sync = reader.read_xml_sync(path)
    reader.save_csv(pd_sync, output_path)


def bva_phases_table():
    # Validations
    path = get_sys_filepath(sys.argv)
    output_path = create_output_path(sys.argv) + 'phases.csv'
    pd_phases = reader.read_xml_phases(path)
    reader.save_csv(pd_phases, output_path)


def bva_measure_start_stop_table():
    # Validations
    path = get_sys_filepath(sys.argv)
    output_path = create_output_path(sys.argv, 'measure_start_stop.csv')
    pd_start_stop = reader.read_measure_start_stop(path)
    reader.save_csv(pd_start_stop, output_path)


def xml_settings_to_csv():
    # Validations
    if (len(sys.argv) < 2):
        sys.exit('You have to provide xml input file')
    else:
        # TODO - issue with comman with single instead of double quotes
        path = os.path.join(os.getcwd(), sys.argv[1])

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
        if (os.path.isabs(args[1])):
            path = args[1]
        # TODO - issue with comman with single instead of double quotes
        else:
            path = os.path.join(os.getcwd(), args[1])
        # check existence
    return(path)


def default_sys_output_argument(args):
    if (len(args) < 3): 
        output_name = ''
    else:
        output_name = args[2] + '_'
    return(output_name)


def create_output_path(args):
    output_name = default_sys_output_argument(args)
    output_path = os.path.dirname(os.path.realpath(get_sys_filepath(args)))
    return(os.path.join(output_path, output_name))