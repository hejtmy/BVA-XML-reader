import os
import click
from bvareader import reader
from bvareader.exporter import save_csv
from bvareader.preprocessing import prepare_position


@click.command()
@click.argument('path', type=click.Path(exists=True), nargs=1)
@click.option('-o', '--output', default='', help='name of the output files')
def process_bva_data(path, output):
    """This script opens given path and outputs a preprocessed
    xml files including positions, measures, phases and sync times"""
    output_path = create_output_path(path, output)
    bva_prepare(path, output_path)


@click.command()
@click.argument('path', type=click.Path(exists=True))
@click.option('-o', '--output', default='', help='name of the output files')
def process_bva_positions(path, output):
    """This script takes given bva xml file and outputs
    preprocessed csv files with positions"""
    output_path = create_output_path(path, output) + 'positions'

    pd_bva = reader.read_positions(path)
    pd_bva2 = prepare_position(pd_bva)

    save_csv(pd_bva, output_path + '_full.csv')
    save_csv(pd_bva2, output_path + '.csv')


@click.command()
@click.argument('path', type=click.Path(exists=True))
@click.option('-o', '--output', default='', help='name of the output files')
def process_bva_sync_times(path, output):
    """This script takes given bva xml file and outputs
    preprocessed csv files with sync times"""
    output_path = create_output_path(path, output) + 'sync_times.csv'
    pd_sync = reader.read_sync_times(path)
    reader.save_csv(pd_sync, output_path)


@click.command()
@click.argument('path', type=click.Path(exists=True))
@click.option('-o', '--output', default='', help='name of the output files')
def process_bva_phases(path, output):
    """This script takes given bva file and outputs
    preprocessed csv files with phases"""
    output_path = create_output_path(path, output) + 'phases.csv'
    pd_phases = reader.read_phases(path)
    save_csv(pd_phases, output_path)


@click.command()
@click.argument('path', type=click.Path(exists=True))
@click.option('-o', '--output', default='', help='name of the output files')
def process_bva_measure_start_stop(path, output):
    """This script takes given bva xml file and outputs
    preprocessed csv files with measure starts and stops"""
    output_path = create_output_path(path, output) + 'measure_start_stop.csv'
    pd_start_stop = reader.read_new_measure_start_stop(path)
    save_csv(pd_start_stop, output_path)


@click.command()
@click.argument('path', type=click.Path(exists=True))
@click.option('-o', '--output', default='settings', help='name of the output files')
def xml_settings_to_csv(path, output):
    # TODO - issue with comman with single instead of double quotes
    output_path = create_output_path(output) + '.csv'
    pd_settings = reader.read_xml_settings(path)
    save_csv(pd_settings, output_path)


def create_output_path(path, output):
    output_prefix = '' if output == '' else output + '_'
    output_path = os.path.dirname(os.path.realpath(path))
    return(os.path.join(output_path, output_prefix))


def bva_prepare(path, output_path):
    pd_bva = reader.read_positions(path)
    pd_bva_prep = prepare_position(pd_bva)
    pd_sync = reader.read_sync_times(path)
    pd_phases = reader.read_phases(path)
    if reader.old_or_new(path) == 'new':
        try:
            pd_start_stop = reader.read_new_measure_start_stop(path)
            save_csv(pd_start_stop, output_path + 'measure_start_stop.csv')
        except(Exception):
            print("Could not process start and stop due to non appropriate data")
            pass
    if reader.old_or_new(path) == 'old':
        try:
            pd_keys = reader.read_keypresses(path)
            save_csv(pd_keys, output_path + 'keypresses.csv')
        except(Exception):
            print("Could not process start and stop due to non appropriate data")
            pass
    save_csv(pd_bva, output_path + 'positions_unprocessed.csv')
    save_csv(pd_bva_prep, output_path + 'positions_processed.csv')
    save_csv(pd_sync, output_path + 'sync_times.csv')
    save_csv(pd_phases, output_path + 'phases.csv')
