import sys
import os
import click
from bvareader import reader
from bvareader.preprocessing import add_rotation
from bvareader.preprocessing import preprocess_bva_data


@click.command()
@click.argument('path', type=click.Path(exists=True), nargs=1)
@click.option('-o', '--output', default='', help='name of the output files')
def sys_bva_preprocess_xml(path, output):
    """This script opens given path and outputs a preprocessed
    xml files including positions, measures, phases and sync times"""
    # Validations
    output_path = create_output_path(path, output)
    bva_preprocess_xml(path, output_path)


@click.command()
@click.argument('path', type=click.Path(exists=True))
@click.option('-o', '--output', default='', help='name of the output files')
def bva_positions_table(path, output):
    """This script takes given bva xml file and outputs
    preprocessed csv files with positions"""
    # Validations
    output_path = create_output_path(output) + 'positions'

    pd_bva = reader.read_xml_bva(path)
    pd_bva = add_rotation(pd_bva)
    pd_bva2 = preprocess_bva_data(pd_bva)

    reader.save_csv(pd_bva, output_path + '_full.csv')
    reader.save_csv(pd_bva2, output_path + '.csv')


@click.command()
@click.argument('path', type=click.Path(exists=True))
@click.option('-o', '--output', default='', help='name of the output files')
def bva_sync_times_table(path, output):
    """This script takes given bva xml file and outputs
    preprocessed csv files with sync times"""
    # Validations
    output_path = create_output_path(output) + 'sync_times.csv'
    pd_sync = reader.read_xml_sync(path)
    reader.save_csv(pd_sync, output_path)


@click.command()
@click.argument('path', type=click.Path(exists=True))
@click.option('-o', '--output', default='', help='name of the output files')
def bva_phases_table(path, output):
    """This script takes given bva xml file and outputs
    preprocessed csv files with phases"""
    # Validations
    output_path = create_output_path(sys.argv) + 'phases.csv'
    pd_phases = reader.read_xml_phases(path)
    reader.save_csv(pd_phases, output_path)


@click.command()
@click.argument('path', type=click.Path(exists=True))
@click.option('-o', '--output', default='', help='name of the output files')
def bva_measure_start_stop_table(path, output):
    """This script takes given bva xml file and outputs
    preprocessed csv files with measure starts and stops"""
    # Validations
    output_path = create_output_path(sys.argv, 'measure_start_stop.csv')
    pd_start_stop = reader.read_measure_start_stop(path)
    reader.save_csv(pd_start_stop, output_path)


@click.command()
@click.argument('path', type=click.Path(exists=True))
@click.option('-o', '--output', default='settings', help='name of the output files')
def xml_settings_to_csv(path, output):
    # TODO - issue with comman with single instead of double quotes
    path = os.path.join(os.getcwd(), sys.argv[1])
    pd_settings = reader.read_xml_settings(path)
    reader.save_csv(pd_settings, output + '.csv')


def create_output_path(path, output):
    output_prefix = '' if output == '' else output + '_'
    output_path = os.path.dirname(os.path.realpath(path))
    return(os.path.join(output_path, output_prefix))


def bva_preprocess_xml(path, output_path):
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
