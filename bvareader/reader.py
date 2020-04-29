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


# OLD BVA ONLY


def read_keypresses(path):
    """Reads keypresses from the TR files.

    Only functions on the old data, as the new data are not bound by keypresses, but events
    Parameters
    ----------
    path : str

    Returns
    -------
    pandas.DataFrame
        returns pandas DataFrame with two columns: key and time
    """
    if old_or_new(path) == 'new':
        raise Exception('Can only be run on old data')
        return
    pd_keys = old_reader.read_keypresses(path)
    return pd_keys


def read_old_settings(path):
    """Reads keypresses from the TR files.

    Only functions on the old data, as the new data are not bound by keypresses, but events
    Parameters
    ----------
    path : str

    Returns
    -------
    pandas.DataFrame
        returns pandas DataFrame with two columns: key and time
    """
    if old_or_new(path) == 'new':
        raise Exception('Can only be run on old data')
        return
    pd_settings = old_reader.read_settings(path)
    return pd_settings


def read_lasers(path):
    """Reads cue laser infromation from the TR file

    It the processed laser information is part of the settings file if everything goes well, but for clarity, it
    can be output as a separate file with all information
    Parameters
    ----------
    path : str

    Returns
    -------
    pandas.DataFrame
        returns pandas DataFrame
    """
    if old_or_new(path) == 'new':
        raise Exception('Can only be run on old data')
        return
    pd_keys = old_reader.read_lasers(path)
    return pd_keys

# NEW BVA ONLY


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
    return pd_phases


def read_new_measure_start_stop(path):
    pd_start_stops = new_reader.read_measure_start_stop(path)
    return pd_start_stops


def read_new_settings(path):
    pd_settings = new_reader.read_xml_settings(path)
    return pd_settings


def read_sync_file(path):
    pd_sync = new_reader.read_sync_file(path)
    return(pd_sync)


# Helpers
def old_or_new(path):
    # TR1, TR3 or TR4 files are the old
    filename, extension = os.path.splitext(path)
    if extension in ['.TR1', '.TR3', '.TR4']:
        return 'old'
    if extension in ['.xml']:
        return 'new'
    # xml files are new
    return None
