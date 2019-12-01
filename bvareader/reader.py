import os
import bvareader.new_bva.reader as new_reader
import bvareader.old_bva.reader as old_reader


def read_positions(path):
    """Reads in positional data from given file

    This function works for both old and new bva data.

    Parameters
    ---------
    path : str
        path to the bva file (xml for new, TR3 for old)

    Returns
    -------
    pandas.DataFrame
        returns pandas Dataframe with unprocessed columns
    """

    if old_or_new(path) == 'new':
        pd_bva = new_reader.read_xml_bva(path)
    if old_or_new(path) == 'old':
        pd_bva = old_reader.read_position(path)
    return pd_bva


def read_sync_times(path):
    """Reads in sync times data from given file

    This function works for both old and new bva data.

    Parameters
    ---------
    path : str
        path to the bva file (xml for new, TR3 for old)

    Returns
    -------
    pandas.DataFrame
        returns pandas Dataframe with timestamps of each given sync time. DataFrame columns differ for
        old and for the new bva
    """

    if old_or_new(path) == 'new':
        pd_times = new_reader.read_xml_sync(path)
    if old_or_new(path) == 'old':
        pd_times = old_reader.read_sync(path)
    return(pd_times)


def read_phases(path):
    """Reads in phase times data from given file

    This function works for both old and new bva data.

    Parameters
    ---------
    path : str
        path to the bva file (xml for new, TR3 for old)

    Returns
    -------
    pandas.DataFrame
        returns pandas Dataframe with loaded information from the file. The DataFrame columns differ for
        old and for the new bva
    """

    if old_or_new(path) == 'new':
        pd_phases = new_reader.read_xml_phases(path)
    if old_or_new(path) == 'old':
        pd_phases = old_reader.read_phases(path)
    return pd_phases


# NEW BVA ONLY


def read_new_measure_start_stop(path):
    pd_start_stops = new_reader.read_measure_start_stop(path)
    return pd_start_stops


def read_new_settings(path):
    pd_settings = new_reader.read_xml_settings(path)
    return pd_settings


def read_sync_file(path):
    pd_sync = new_reader.read_sync_file(path)
    return(pd_sync)


def old_or_new(path):
    # TR3 or TR4 files are the old
    filename, extension = os.path.splitext(path)
    if extension in ['.TR3', '.TR4']:
        return 'old'
    if extension in ['.xml']:
        return 'new'
    # xml files are new
    return None
